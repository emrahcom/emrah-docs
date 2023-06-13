## Debian Bookworm Installation

### netinstall

- Select a language: `English`
- Select your location: `other -> Asia -> Turkey`
- Configure locales: `United States en_US.UTF-8`
- Additional locales: `tr_TR.UTF-8`
- System Locale: `en_US.UTF-8`
- Select a keyboard layout: `PC-style -> Turkish (Q layout)`
- Configure the network: `DHCP`
- Configure the clock (time zone): `Europe/Istanbul`
- Partitition disks: `manual`
- Partition table: `gpt`

Partitions

- /efi
  - 512 MB
  - bootable
- /boot
  - 512 MB
- crypto
  - `total - swap` GB
  - /
- swap
  - at least 8 GB
  - No swap during the installation.

### base repo

#### initial packages

```bash
apt-get update
apt-get autoclean
apt-get dist-upgrade
apt-get autoremove --purge

apt-get install zsh tmux vim autojump
apt-get install openssh-server
apt-get install net-tools bridge-utils

apt-get purge installation-report reportbug nano
apt-get purge os-prober
apt-get autoremove --purge
```

#### /etc/apt/sources.list

```
deb http://deb.debian.org/debian/ bookworm main non-free-firmware
deb http://security.debian.org/debian-security bookworm-security main non-free-firmware
deb http://deb.debian.org/debian/ bookworm-updates main non-free-firmware
```

#### /etc/apt/apt.conf.d/80recommends

```
APT::Install-Recommends "0";
APT::Install-Suggests "0";
```

#### repo update

```bash
apt-get update
```

### base config

#### SSH public keys

Put public SSH keys if needed.

```bash
ssh localhost
cat /tmp/gnu.pub >>.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys
```

#### /etc/ssh/sshd_config.d/emrah.conf

```
Port 22
PasswordAuthentication no
GatewayPorts yes
```

#### rc files

```bash
chsh -s /bin/zsh emrah
chsh -s /bin/zsh root

su -l emrah
# (2)  Populate your...
```

##### .bashrc

```
export TMOUT=1800
```

##### .tmux.conf

```
bind '"' split-window -c "#{pane_current_path}"
bind % split-window -h -c "#{pane_current_path}"
bind c new-window -c "#{pane_current_path}"
set -g history-limit 10000
```

##### .vimrc

Check `vim` notes. `root` and `emrah` have different versions of `.vimrc`.

##### .zshrc

```
#bindkey -e
bindkey -v

export TMOUT=1800
setopt hist_ignore_space

alias ls='ls --color=auto'
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias .....="cd ../../../.."
alias ......="cd ../../../../.."
source /usr/share/autojump/autojump.sh
```
