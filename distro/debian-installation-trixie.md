## Debian Trixie Installation

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

#### Partitions

- /efi
  - 1 GB
  - bootable
- /boot
  - 1 GB
- crypto
  - `total - swap` GB
  - /
  - Reserved block: 1%
- swap
  - at least 8 GB
  - No swap during the installation

### base repo

#### initial packages

```bash
apt modernize-sources
rm /etc/apt/sources.list.bak
rm /etc/apt/sources.list~

apt-get update
apt-get autoclean
apt-get dist-upgrade
apt-get autoremove --purge

apt-get install zsh tmux vim autojump fzf
apt-get install openssh-server
apt-get install parted

touch /root/.vimrc

apt-get purge installation-report reportbug nano
apt-get purge os-prober
apt-get autoremove --purge
```

#### /etc/apt/sources.list.d/debian.sources

```
Types: deb
URIs: http://deb.debian.org/debian/
Suites: trixie
Components: main non-free-firmware
Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg

Types: deb
URIs: http://security.debian.org/debian-security/
Suites: trixie-security
Components: main non-free-firmware
Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg

Types: deb
URIs: http://deb.debian.org/debian/
Suites: trixie-updates
Components: main non-free-firmware
Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg
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

#### swap

```bash
fdisk -lc

parted /dev/nvme0n1
  unit s
  p
  p free
  mkpart
    Partition name?  []?
    File system type?  [ext2]? linux-swap
    Start? xxx
    End? 100%
  q

fdisk -l
mkswap /dev/nvme0n1p4
swapon /dev/nvme0n1p4
free -m
```

##### /etc/fstab

```
/dev/nvme0n1p4  none            swap sw 0 0
```

#### grub

##### /etc/default/grub

```
GRUB_TIMEOUT=1
```

```bash
update-grub
```

#### ctrl + alt + del

```bash
ln -s /lib/systemd/system/poweroff.target \
  /etc/systemd/system/ctrl-alt-del.target

systemctl daemon-reload
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

##### .zshrc (root)

```
#bindkey -e
bindkey -v

alias ls='ls --color=auto'
alias vv='vim $(fzf)'
alias cdf='cd $(find . -type d | fzf)'
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias .....="cd ../../../.."
alias ......="cd ../../../../.."
alias .......="cd ../../../../../.."
alias ........="cd ../../../../../../.."
alias .........="cd ../../../../../../../.."
alias ..........="cd ../../../../../../../../.."
alias ...........="cd ../../../../../../../../../.."
alias ............="cd ../../../../../../../../../../.."
alias .............="cd ../../../../../../../../../../../.."
alias ..............="cd ../../../../../../../../../../../../.."
source /usr/share/autojump/autojump.sh
source /usr/share/doc/fzf/examples/key-bindings.zsh

export TMOUT=1800
setopt autocd
setopt hist_ignore_space
```

##### .zshrc (emrah)

```
#bindkey -e
bindkey -v

HISTSIZE=10000
SAVEHIST=10000

chronometer() {
  stf=$(date +%s.%N)
  for ((;;))
  do
    ctf=$( date +%s.%N )
    echo -en "\r$(date -u -d "0 $ctf sec - $stf sec" "+%H:%M:%S.%N")"
  done
}

export TMOUT=1800
export GPG_TTY=$(tty)
export PATH=$PATH:~/bin

setopt autocd
setopt hist_ignore_space

alias x='ssh-agent startx'
alias g='ssh-add ~/.ssh/gnu'
alias vv='vim $(fzf)'
alias cdf='cd $(find . -type d | fzf)'

alias ls='ls --color=auto'
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias .....="cd ../../../.."
alias ......="cd ../../../../.."
alias .......="cd ../../../../../.."
alias ........="cd ../../../../../../.."
alias .........="cd ../../../../../../../.."
alias ..........="cd ../../../../../../../../.."
alias ...........="cd ../../../../../../../../../.."
alias ............="cd ../../../../../../../../../../.."
alias .............="cd ../../../../../../../../../../../.."
alias ..............="cd ../../../../../../../../../../../../.."

source /usr/share/autojump/autojump.sh
source /usr/share/doc/fzf/examples/key-bindings.zsh

if [[ -n "$DISPLAY" ]]; then
  xset r rate 250 40
fi
```

### packages

#### /etc/apt/sources.list.d/debian.sources

```
Types: deb
URIs: http://deb.debian.org/debian/
Suites: trixie
Components: main non-free-firmware
Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg

Types: deb
URIs: http://security.debian.org/debian-security/
Suites: trixie-security
Components: main non-free-firmware
Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg

Types: deb
URIs: http://deb.debian.org/debian/
Suites: trixie-updates
Components: main non-free-firmware
Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg
```

```bash
apt-get update
apt-get install gnupg
apt-get install git patch
apt-get install ack jq unzip
apt-get install net-tools curl rsync bridge-utils
apt-get install ngrep whois fping netcat-openbsd htop
apt-get install sudo encfs
apt-get install lxc debootstrap
apt-get install mpv ffmpeg
apt-get install --install-recommends pipewire-audio
apt-get install pulseaudio-utils
```

#### /etc/apt/sources.list.d/nodesource.sources

See also [nodejs](/development/nodejs.md)

```
Types: deb
URIs: https://deb.nodesource.com/node_22.x/
Suites: nodistro
Components: main
Signed-By: /usr/share/keyrings/nodesource.gpg
```

```bash
wget -qO /tmp/nodesource.gpg.key \
  https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key
cat /tmp/nodesource.gpg.key | gpg --dearmor \
  >/usr/share/keyrings/nodesource.gpg

apt-get update
apt-get install nodejs

nodejs --version
```

#### /etc/apt/sources.list.d/yarn.sources

```
Types: deb
URIs: https://dl.yarnpkg.com/debian/
Suites: stable
Components: main
Signed-By: /usr/share/keyrings/yarn.gpg
```

```bash
wget -qO /tmp/yarn.gpg.key https://dl.yarnpkg.com/debian/pubkey.gpg
cat /tmp/yarn.gpg.key | gpg --dearmor >/usr/share/keyrings/yarn.gpg

apt-get update
apt-get install yarn

yarn --version
```

#### deno

```bash
cd /tmp
wget -T 30 -O deno.zip https://github.com/denoland/deno/releases/latest/download/deno-x86_64-unknown-linux-gnu.zip
unzip deno.zip
./deno --version

cp /tmp/deno /usr/local/bin/
deno --version
```

### network

#### /etc/default/lxc-net

```
#USE_LXC_BRIDGE="true"
USE_LXC_BRIDGE="false"
```

#### /etc/network/interfaces

```
# The primary wireless interface
allow-hotplug wlan0
iface wlan0 inet dhcp
```

#### iwd

```bash
apt-get purge wpasupplicant
apt-get autoremove --purge

apt-get install iwd rfkill

systemctl disable iwd.service

rfkill list all
rfkill unblock <ID>
```

If `iwd` is enabled by default, it slows down the boot. Start it later while
loading the desktop. Allow user to control the service with
`visudo /etc/sudoers.d/emrah`

```
emrah   ALL=NOPASSWD:/usr/bin/systemctl restart iwd.service
emrah   ALL=NOPASSWD:/usr/bin/systemctl start iwd.service
emrah   ALL=NOPASSWD:/usr/bin/systemctl status iwd.service
emrah   ALL=NOPASSWD:/usr/bin/systemctl stop iwd.service
emrah   ALL=NOPASSWD:/usr/bin/systemctl restart em-sock
emrah   ALL=NOPASSWD:/usr/bin/brightnessctl
```

```bash
su -l emrah
sudo /usr/bin/systemctl start iwd.service
iwctl
  station list
  station wlan0 scan
  station wlan0 get-networks
  station wlan0 connect <NETWORK>
```

#### /etc/network/interfaces.d/bridge_br0.cfg

```
# private dummy interface
auto edummy0
iface edummy0 inet manual
pre-up /sbin/ip link add edummy0 type dummy
up /sbin/ip link set edummy0 address 52:54:05:20:06:32

# private bridge
auto br0
iface br0 inet static
address 172.17.17.1
netmask 255.255.255.0
bridge_ports edummy0
bridge_stp off
bridge_fd 0
bridge_maxwait 0

# routing for css development environment
post-up ip route add 192.168.90.0/24 via 172.17.17.50
pre-down ip route del 192.168.90.0/24 via 172.17.17.50
```

#### /etc/network/interfaces.d/bridge_br1.cfg

```
# private dummy interface
auto edummy1
iface edummy1 inet manual
pre-up /sbin/ip link add edummy1 type dummy
up /sbin/ip link set edummy1 address 52:54:05:20:06:34

# private bridge
auto br1
iface br1 inet static
address 172.18.18.1
netmask 255.255.255.0
bridge_ports edummy1
bridge_stp off
bridge_fd 0
bridge_maxwait 0
```

#### /etc/sysctl.d/90-ip-forward.conf

```
net.ipv4.ip_forward=1
```

#### dnsmasq

```bash
apt-get install dnsmasq
```

##### /etc/dnsmasq.d/my-networks

```
bind-interfaces
interface=br0
interface=br1
resolv-file=/etc/resolv.conf

# br0
dhcp-range=interface:br0,172.17.17.100,172.17.17.200,48h
dhcp-option=interface:br0,option:dns-server,172.17.17.1

# br1
dhcp-range=interface:br1,172.18.18.100,172.18.18.200,48h
dhcp-option=interface:br1,option:dns-server,172.18.18.1

# br0 static addresses
address=/postgres.mydomain.loc/172.17.17.20

# br1 static addresses
address=/ucs.mydomain.corp/172.18.18.20
```

##### /etc/dhcpcd.conf

```
# emrah: dont update resolv.conf
nohook resolv.conf
```

##### /etc/resolv.conf

Check and set its content after the next reboot.

```
nameserver 127.0.0.1
nameserver 172.17.17.1
nameserver 172.18.18.1
nameserver 1.1.1.1
nameserver 208.67.222.222
nameserver 8.8.8.8
```

##### /etc/resolv.conf.head

Use the same content with /etc/resolv.conf.

Actually it will not have an effect in this config since `nohook` is set in
`dhcpcd.conf`.

#### /etc/nftables.conf

Use `tab` for spaces.

```
#!/usr/sbin/nft -f

flush ruleset

table inet filter {
        chain input {
                type filter hook input priority filter;
        }
        chain forward {
                type filter hook forward priority filter;
        }
        chain output {
                type filter hook output priority filter;
                iifname "enp*" ip daddr 172.17.17.0/24 drop;
                iifname "enp*" ip daddr 172.18.18.0/24 drop;
                iifname "wlan*" ip daddr 172.17.17.0/24 drop;
                iifname "wlan*" ip daddr 172.18.18.0/24 drop;
                #udp dport 10000 drop;
        }
}

table ip nat {
        chain postrouting {
                type nat hook postrouting priority filter;
                ip saddr 172.17.17.0/24 masquerade;
                ip saddr 172.18.18.0/24 masquerade;
        }
}
```

Enable and start the service:

```bash
systemctl enable nftables
systemctl start nftables
```

### applications

#### desktop

```bash
apt-get install --install-recommends xorg
apt-get install --install-recommends spectrwm
apt-get install --install-recommends firefox-esr
apt-get install --install-recommends chromium chromium-sandbox
apt-get install --install-recommends libreoffice
apt-get install --install-recommends gimp
apt-get install dbus-x11
apt-get install xterm
apt-get install xtrlock unclutter
apt-get install brightnessctl
apt-get install scrot
apt-get install pavucontrol
apt-get install x11vnc xtightvncviewer
apt-get install zathura
```

### user

#### archieves

Copy archieves from the current device.

```bash
IP=192.168.1.124

ssh -l emrah ${IP} -- mkdir -p ~/.config ~/bin
rsync -avhe 'ssh -l emrah' .config/git ${IP}:~/.config/
rsync -avhe 'ssh -l emrah' .gitconfig ${IP}:~/
rsync -avhe 'ssh -l emrah' .gnupg ${IP}:~/
rsync -avhe 'ssh -l emrah' .ssh ${IP}:~/
rsync -avhe 'ssh -l emrah' archive ${IP}:~/
rsync -avhe 'ssh -l emrah' bin ${IP}:~/
rsync -avhe 'ssh -l emrah' conceptboard ${IP}:~/
rsync -avhe 'ssh -l emrah' downloads ${IP}:~/
rsync -avhe 'ssh -l emrah' git-repo ${IP}:~/
rsync -avhe 'ssh -l emrah' installer ${IP}:~/
rsync -avhe 'ssh -l emrah' media ${IP}:~/
rsync -avhe 'ssh -l emrah' nordeck ${IP}:~/
rsync -avhe 'ssh -l emrah' test ${IP}:~/

rsync -avhe 'ssh -l emrah' .config/chromium* ${IP}:~/.config/
```

Testing on the new device:

```bash
su -l emrah
ssh-agent bash
ssh-add .ssh/gnu

cd ~/git-repo
./pull.sh

cd ~/conceptboard/repo
./pull.sh

cd ~/nordeck/repo
./pull.sh
```

#### wireplumber

It should be the native user shell, no `su -l`...

```bash
systemctl --user --now enable wireplumber.service
```

#### .Xdefaults

```
#UXTerm*background: white
#UXTerm*foreground: black
#UXTerm*faceSize: 18
UXTerm*background: black
UXTerm*foreground: green
UXTerm*faceName: DejaVu Sans Mono
UXTerm*faceSize: 14
UXTerm*termName: xterm-256color
UXTerm*on2Clicks: word
UXTerm*on3Clicks: regex [^ \n]+
UXTerm*on4Clicks: regex [^'"(){}\n]+
UXTerm*on5Clicks: regex [^\n]+
```

```bash
ln -s .Xdefaults ~/.Xdefaults-$(hostname)
```

#### .spectrwm.conf

```bash
cp /etc/spectrwm.conf .spectrwm.conf
```

```
program[screenshot_all] = bash -c "mkdir -p /tmp/scrot; scrot /tmp/scrot/$(date +'%Y-%m-%d-%H%M%S').png"
disable_border          = 1
bar_at_bottom           = 1
maximize_hide_bar       = 1
bar_font                = DejaVu Sans Mono:pixelsize=20:antialias=true
bar_font_color[]        = rgb:00/d8/00
clock_format            = %a %b %d %T

modkey = Mod4

program[lock]           = xtrlock
program[firefox]        = firefox-esr
bind[firefox]           = MOD+shift+f
program[pavucontrol]    = pavucontrol
bind[pavucontrol]       = MOD+shift+a
program[python3]        = x-terminal-emulator -e /usr/bin/python3
bind[python3]           = MOD+shift+p

program[chromium]       = chromium --user-data-dir=.config/chromium.default --proxy-server="socks5://127.0.0.1:65022" --proxy-bypass-list="localhost;127.0.0.1/8;192.168.0.0/16;172.16.0.0/12;10.0.0.0/8;*.corp;*.loc;*.local;*.internal;*.yourdomain.com;"
bind[chromium]          = MOD+shift+c

program[chromium.cb]    = chromium --user-data-dir=.config/chromium.conceptboard"
bind[chromium.cb]       = MOD+shift+m

program[chromium.no]    = chromium --user-data-dir=.config/chromium.nordeck"
bind[chromium.no]       = MOD+shift+n
```

#### .xinitrc

```
sudo /usr/bin/systemctl start iwd.service
#mozilla2ram
xset r rate 250 40
exec /usr/bin/spectrwm
```

#### commands for history

```bash
sudo brightnessctl
sudo brightnessctl s 9000

setxkbmap us
```

#### other applications

Use seperate docs

- em-sock
- em-vpn
- [firefox config](/applications/firefox.md)
- thunderbird
- [docker](/applications/docker-trixie.md)
- [libvirt](/applications/libvirt.md)
- [adb](/applications/adb.md)
- minikube (in minikube VM)
- kubectl (in minikube VM)
- helm (in minikube VM)
- linphone (when needed)
- apt-cacher (?)
- lxc template containers (?)

#### web applications

- Outlook
- Teams
- Jira
- Holasprit

- Translate
- Matrix
- WhatsApp
- Teams (Skype)
- Speak
- Exchange
- Conversation
- InterPals
- ChatGPT
- Gemini
- Deepseek
- Claude

- Jitok
- Google
