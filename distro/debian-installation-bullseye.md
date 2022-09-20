## Debian Bullseye Installation

#### netinstall

- Select a language: _English_
- Select your location: _other -> Asia -> Turkey_
- Configure locales: _United States en_US.UTF-8_
- Additional locales: _tr_TR.UTF-8_
- System Locale: _en_US.UTF-8_
- Select a keyboard layout: _PC-style -> Turkish (Q layout)_
- Configure the network: _DHCP_
- Configure the clock (time zone): _Europe/Istanbul_
- Partitition disks: _manual_
- Partition table: _gpt_

Partitions

- /efi | 600 MB | sda1 | bootable
- /boot | 200 MB | sda2
- crypto | X GB | sda3 | mount to /

No swap during the installation.

#### base system

##### initial packages

```bash
apt-get update
apt-get autoclean
apt-get dist-upgrade
apt-get autoremove --purge

apt-get install zsh tmux vim autojump
apt-get install openssh-server
apt-get install procps net-tools bridge-utils

apt-get purge installation-report reportbug nano
apt-get purge os-prober
apt-get autoremove --purge
```

##### /etc/apt/sources.list

```
deb https://deb.debian.org/debian bullseye main non-free contrib
deb-src https://deb.debian.org/debian bullseye main non-free contrib

deb https://deb.debian.org/debian bullseye-updates main non-free contrib
deb-src https://deb.debian.org/debian bullseye-updates main non-free contrib

deb https://security.debian.org/debian-security bullseye-security main contrib non-free
deb-src https://security.debian.org/debian-security bullseye-security main contrib non-free
```

##### /etc/apt/apt.conf.d/80recommends

```
APT::Install-Recommends "0";
APT::Install-Suggests "0";
```

##### repo update

```bash
apt-get update
```

##### /etc/ssh/sshd_config.d/emrah.conf

```conf
Port 22
PasswordAuthentication no
GatewayPorts yes
```

#### packages

##### tools

```bash
apt-get install gnupg jq
```

##### nodejs

```bash
wget -qO /tmp/nodesource.gpg.key \
    https://deb.nodesource.com/gpgkey/nodesource.gpg.key
cat /tmp/nodesource.gpg.key | gpg --dearmor \
    >/usr/share/keyrings/nodesource.gpg
echo "deb [signed-by=/usr/share/keyrings/nodesource.gpg] \
    https://deb.nodesource.com/node_16.x bullseye main" \
    >/etc/apt/sources.list.d/nodesource.list

apt-get update
apt-get install nodejs
```

##### google chrome

For reference... Don't install, use `chromium`

```bash
wget -qO /tmp/google-chrome.gpg.key \
    https://dl.google.com/linux/linux_signing_key.pub
cat /tmp/google-chrome.gpg.key | gpg --dearmor \
    >/usr/share/keyrings/google-chrome.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg]" \
    "https://dl.google.com/linux/chrome/deb/ stable main" \
    >/etc/apt/sources.list.d/google-chrome.list

apt-get update
apt-get --install-recommends install google-chrome-stable

apt-key finger
apt-key remove "google fingerprint"
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg]" \
    "https://dl.google.com/linux/chrome/deb/ stable main" \
    >/etc/apt/sources.list.d/google-chrome.list
```

`~/.spectrwm.conf`

```conf
program[chrome]= google-chrome
bind[chrome]   = MOD+shift+c
```

##### ungoogled-chromium

For reference... Don't install, use `chromium`

```bash
wget -qO /tmp/ungoogled-chromium.gpg.key \
    https://download.opensuse.org/repositories/home:/ungoogled_chromium/Debian_Bullseye/Release.key
cat /tmp/ungoogled-chromium.gpg.key | gpg --dearmor \
    >/usr/share/keyrings/ungoogled-chromium.gpg
echo "deb [signed-by=/usr/share/keyrings/ungoogled-chromium.gpg]" \
    "http://download.opensuse.org/repositories/home:/ungoogled_chromium/Debian_Bullseye/" \
    "/" >/etc/apt/sources.list.d/ungoogle-chromium.list

apt-get update
apt-get install libgtk-3-0
apt-get install ungoogled-chromium
```

##### element-desktop

```bash
wget -O /usr/share/keyrings/element-io-archive-keyring.gpg \
    https://packages.element.io/debian/element-io-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/element-io-archive-keyring.gpg]" \
    "https://packages.element.io/debian/ default main" \
    >/etc/apt/sources.list.d/element.list

apt-get update
apt-get install element-desktop
```

`~/.spectrwm.conf`

```conf
program[element-desktop]= element-desktop
bind[element-desktop]   = MOD+shift+m
```

##### /etc/network/interfaces.d/bridge_br0.cfg

```conf
# private dummy interface
auto edummy0
iface edummy0 inet manual
pre-up /sbin/ip link add edummy0 type dummy
up /sbin/ip link set edummy0 address 52:54:05:22:06:30

# private bridge
auto br0
iface br0 inet static
address 172.17.17.1
netmask 255.255.255.0
bridge_ports edummy0
bridge_stp off
bridge_fd 0
bridge_maxwait 0
```

#### services

##### iwd

```bash
apt-get purge wpasupplicant
apt-get autoremove --purge

apt-get install iwd
```

_/etc/network/interfaces_

```conf
allow-hotplug wlan0
iface wlan0 inet dhcp
```

Disable autostart otherwise causes slow boot.

```bash
systemctl disable iwd.service
```

visudo

```
emrah   ALL=NOPASSWD:/usr/bin/systemctl start iwd.service
emrah   ALL=NOPASSWD:/usr/bin/systemctl stop iwd.service
emrah   ALL=NOPASSWD:/usr/bin/systemctl restart iwd.service
```

#### desktop

_/home/emrah/.xinitrc_

```
sudo /usr/bin/systemctl start iwd.service
mozilla2ram
xset r rate 250 40
exec /usr/bin/spectrwm
```

#### applications

##### firefox-esr

- read aloud
  - increase the speed
  - edit shortcuts
    - play/pause ALT+L
    - stop ALT+k

##### chromium

```bash
apt-get install chromium chromium-sandbox
```

`~/.spectrwm.conf`

```conf
program[chromium]= chromium
bind[chromium]   = MOD+shift+c
```

##### zsh

`~/.zshrc`

```bash
alias x='ssh-agent startx'
alias startx='ssh-agent startx'
alias xoutput='xrandr --output eDP-1 --mode 1368x768 --primary --output DP-1 --auto --scale 1x1 --left-of eDP-1 --output HDMI-1 --auto --scale 1x1 --left-of eDP-1'
alias xoutput2='xrandr --output eDP-1 --auto --primary --output DP-1 --auto --scale 1x1 --left-of eDP-1 --output HDMI-1 --auto --scale 1x1 --left-of eDP-1'
alias xmirror='xrandr --output eDP-1 --auto --primary --output HDMI-1 --auto --scale-from 1366x768 --same-as eDP-1'

alias ls='ls --color=auto'
alias vv='vim $(fzf)'
alias cdf='cd $(find . -type d | fzf)'
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias .....="cd ../../../.."
alias ......="cd ../../../../.."
source /usr/share/autojump/autojump.sh
source /usr/share/doc/fzf/examples/key-bindings.zsh

export PATH=$PATH:~/bin
export TMOUT=1800
setopt autocd
setopt hist_ignore_space
export GPG_TTY=$(tty)
```
