## WSL
### Forwarding COM Port / USB
**Method**
https://devblogs.microsoft.com/commandline/connecting-usb-devices-to-wsl/
**Powershell Setup**
```powershell
# Run code $profile in powershell and add these lines
Function ListUSB { usbipd wsl list }

New-Alias -Name lsusb -Value ListUSB

  

Function AttachUSB { usbipd wsl attach -b $args[0] }

New-Alias -Name attach -Value AttachUSB

  

Function DetachUSB { usbipd wsl detach -b $args[0] }

New-Alias -Name detach -Value DetachUSB
```

### ESP-IDF in VSCode WSL
https://github.com/espressif/vscode-esp-idf-extension/blob/master/docs/WSL.md