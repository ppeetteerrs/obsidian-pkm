## Preface
WSL2 is great and ever improving (if it solves the issues related to Serial Port Forwarding, CUDA without Docker and GUI). Sometimes we might want to SSH into our WSL2 machine remotely (for some peculiar reasons), e.g.:
> I want to quickly `rsync` files from remote host into my local machine (and I don't care about security), so I want to use SSH with a fast cipher. Sadly, I don't have admin rights on the remote host, may be I can instead run `rsync` from the remote host into my WSL2 instance!

*Disclaimer: most contents are reference from [here](https://medium.com/@gilad215/ssh-into-a-wsl2-host-remotely-and-reliabley-578a12c91a2)*

## Setup

Install OpenSSH server:
```bash
# Inside your WSL2 distro
sudo apt install openssh-server
```

Listen to port (not 22 since it is used by Windows):
```txt
# /etc/ssh/sshd_config
Port 2222  
ListenAddress 0.0.0.0  
PasswordAuthentication yes
```

Remove password requirement to start `ssh` service (for automation script), and start `ssh`:
```bash
sudo ALL=NOPASSWD: /usr/sbin/service ssh *
service ssh start
```

Forward ports using the automation script (Edit `$Ports` as needed, save as `wsl_ssh.ps1`  and run it):
```powershell
# Start SSH Service.
wsl sudo service ssh start

# WSL2 network port forwarding script v1
#   for enable script, 'Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser' in Powershell,
#   for delete exist rules and ports use 'delete' as parameter, for show ports use 'list' as parameter.
#   written by Daehyuk Ahn, Aug-1-2020

# Display all portproxy information
If ($Args[0] -eq "list") {
    netsh interface portproxy show v4tov4;
    exit;
} 

# If elevation needed, start new process
If (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator))
{
  # Relaunch as an elevated process:
  Start-Process powershell.exe "-File",('"{0}"' -f $MyInvocation.MyCommand.Path),"$Args runas" -Verb RunAs
  exit
}

# You should modify '$Ports' for your applications 
$Ports = (2222,80,443,8080)

# Check WSL ip address
wsl hostname -I | Set-Variable -Name "WSL"
$found = $WSL -match '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}';
if (-not $found) {
  echo "WSL2 cannot be found. Terminate script.";
  exit;
}

# Remove and Create NetFireWallRule
Remove-NetFireWallRule -DisplayName 'WSL 2 Firewall Unlock';
if ($Args[0] -ne "delete") {
  New-NetFireWallRule -DisplayName 'WSL 2 Firewall Unlock' -Direction Outbound -LocalPort $Ports -Action Allow -Protocol TCP;
  New-NetFireWallRule -DisplayName 'WSL 2 Firewall Unlock' -Direction Inbound -LocalPort $Ports -Action Allow -Protocol TCP;
}

# Add each port into portproxy
$Addr = "0.0.0.0"
Foreach ($Port in $Ports) {
    iex "netsh interface portproxy delete v4tov4 listenaddress=$Addr listenport=$Port | Out-Null";
    if ($Args[0] -ne "delete") {
        iex "netsh interface portproxy add v4tov4 listenaddress=$Addr listenport=$Port connectaddress=$WSL connectport=$Port | Out-Null";
    }
}

# Display all portproxy information
netsh interface portproxy show v4tov4;

# Give user to chance to see above list when relaunched start
If ($Args[0] -eq "runas" -Or $Args[1] -eq "runas") {
  Write-Host -NoNewLine 'Press any key to close! ';
  $null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown');
}
```

**Important:** This automation script does not work when Docker WSL backend is running. Turn off Docker's `Use WSL Backend`, disable it for all WSL distros and delete the Docker WSL folders (enter `Linux` in File Explorer address bar) before running the script. You can turn Docker back on afterwards.


Remember to use `-p 2222` when SSH-ing into your WSL2 :)