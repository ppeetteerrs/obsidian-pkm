## OS Installation
1. Download [Ubuntu Server](https://ubuntu.com/download/server)
2. Create a bootable USB using balenaEtcher
3. Go to your PC's BIOS and enable Booting from Storage Device (UEFI)
4. Insert USB, reboot and select USB as boot medium (or drag to top and reboot)
5. Follow the on-screen instructions to install Ubuntu Server, below are my preferences
    - Use whole SSD disk, no logical volumes (it is just a mess to manage, so painful when upgrading SSDs)
    - No pre-installed packages
    - Ethernet connection only
    - Install OpenSSH without importing identity

*Note: it takes quite some time to reach the installation screen, be patient and don't panic if you see stuff like `stdin: invalid argument`*

## Admin User Setup

### Install Essentials
```bash
sudo apt-get -y update && sudo apt-get -y upgrade
sudo apt-get install -y build-essential
```

### Install NVIDIA Driver
```bash
sudo apt-get install -y nvidia-driver-495
sudo reboot
```

### Install Docker
Add Docker repo:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \ "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \ $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Install Docker:
```bash
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.i
```

### Install NVIDIA Container Toolkit
Setup `stable` repository and GPG key:
```bash
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
   && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
   && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
```

Install `nvidia-docker2`:
```bash
sudo apt-get update
sudo apt-get install -y nvidia-docker2
```

Restart Docker and test:
```bash
sudo systemctl restart docker
sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
```

### Formatting Data Drive(s)
> For example, if your SSD is /dev/nvme0n1. [ref](https://linuxconfig.org/partitioning-and-formatting-of-samsung-ssd-850-pro-with-linux)

Start interation:
```bash
sudo fdisk /dev/nvme0n1
```

Dialogue:
```text
Command (m for help): n
Select (default p): p
Partition number (1-4, default 1): 1
Command (m for help): w
```

Make filesystem:
```bash
sudo mkfs -t ext4 /dev/nvme0n1p1
```

### Automount Data Drive(s)
Find data partition:
```bash
sudo fdisk -l
```

Find UUID of data partition:
```bash
sudo blkid
```

Create mount point:
```bash
sudo mkdir /data
```

Add `fstab` entry:
```bash
sudo nano /etc/fstab
```

Add the entry:
```text
UUID=14D82C19D82BF81E /data    auto defaults 0 0
```
- `UUID`: safer to use UUID than e.g. `/dev/sdb` because UUID never changes
- `/data`: mount point
- `auto`: automatically determine filesystem
- `defaults`: default options
- `0`: determines which filesystems need to be dumped (default is `0`)
- `0`: determine the order in which filesystem checks are done at boot time (default is `0`)

Change permissions and mount all:
```bash
sudo chmod -R 777 /data
sudo mount -a
```

### Prevent sleep
```bash
sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target
sudo reboot
```

### Install ZSH and Starship
```bash
sudo apt-get install -y zsh
sh -c "$(curl -fsSL https://starship.rs/install.sh)"
```

## New User Setup (by admin)
> These steps assume that you have created a new user with a home directory. These steps should also be run for the admin user.

- Add SSH public key: `<home_dir>/.ssh/authorized_keys`
- Add user to docker group: `sudo usermod -aG docker <user>` (use `newgrp docker` to activate new group without logging out)
- Add user to data directory: `sudo usermod -aG data <user>`


## New User Setup (by user)
> These steps should also be run for the admin user.

### Oh-my-zsh
Install Oh-my-zsh and plugins:
```bash
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

Change default shell:
```bash
chsh -s $(which zsh)
```

Sample `~/.zshrc`:
```bash
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="robbyrussell"

export HISTSIZE=1000000
export SAVEHIST=1000000
setopt INC_APPEND_HISTORY
setopt HIST_IGNORE_DUPS
setopt EXTENDED_HISTORY

plugins=(
 zsh-syntax-highlighting
 zsh-autosuggestions
)  

source $ZSH/oh-my-zsh.sh
```

### Starship
Add this to `~/.zshrc`:
```bash
eval "$(starship init zsh)"
```

Sample `~/.config/starship.toml`:
```toml
[username]
disabled = true

[hostname]
disabled = true

[conda]
format = "\\([[$style|$environment]]\\) "
ignore_base = false

[git_status]
conflicted = "⚔️ "
ahead = "🔺×$count "
behind = "🔻×$count "
diverged = "🔀 🔺×${ahead_count} 🔻×${behind_count} "
untracked = "🔓×$count "
stashed = "📥 "
modified = "📝×$count "
staged = "🔒×$count "
renamed = ""
deleted = "🔥×$count "
style = "bright-white"
format = "$all_status$ahead_behind"
```

### Install Mambaforge
Installation:
```bash
wget https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh
bash Mambaforge-$(uname)-$(uname -m).sh
```

Setup (please re-open your shell):
```bash
mamba init --all
rm Mambaforge-$(uname)-$(uname -m).sh
conda config --set changeps1 False
```

### Shell Alias
Add this to `~/.zshrc`:
```bash
source $HOME/.local/.shellrc
```

Sample `$HOME/.local/.shellrc`:
```bash
extract() {
        for archive in $*; do
                if [ -f $archive ]; then
                        case $archive in
                        *.tar.bz2) tar xvjf $archive ;;
                        *.tar.gz) tar xvzf $archive ;;
                        *.tar.xz) tar xvf $archive ;;
                        *.bz2) bunzip2 $archive ;;
                        *.rar) rar x $archive ;;
                        *.gz) gunzip $archive ;;
                        *.tar) tar xvf $archive ;;
                        *.tbz2) tar xvjf $archive ;;
                        *.tgz) tar xvzf $archive ;;
                        *.zip) unzip $archive ;;
                        *.Z) uncompress $archive ;;
                        *.7z) 7z x $archive ;;
                        *) echo "don't know how to extract '$archive'..." ;;
                        esac
                else
                        echo "'$archive' is not a valid file!"
                fi
        done
}

# Git
alias ga="git add -A"
alias gc="git commit -m"
alias gac="git add -A && git commit -m"
alias grm="git rm -r --cached ."
alias gp="git push --tags"
alias gir="git rebase -i HEAD~15"

# List
alias l="ls -lAh"
alias cp="cp -r"
alias mk="mkdir -p"
alias rm="rm -rf --preserve-root"

# Apt-get
alias i="sudo apt-get install -y"
alias update="sudo apt-get update -y && sudo apt-get upgrade -y"

# Mamba
alias mi="mamba install -y -c conda-forge"
alias ma="mamba activate"
alias mc="mamba create python=3.9 jupyter notebook flake8 autopep8 pandas numpy scipy matplotlib seaborn -y -n"
alias mcf="mamba env create -f env.yaml"
alias mu="mamba env update -f env.yaml --prune"

# History
alias hg="history | rg"

# RC
alias zrc="code ~/.zshrc"
alias brc="code ~/.bashrc"
alias src="source ~/.zshrc"

# Utils
alias tv="tidy-viewer"
alias machine="macchina"
alias bw="bandwhich"
```