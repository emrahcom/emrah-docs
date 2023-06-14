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

#### Partitions

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

apt-get install zsh tmux vim autojump fzf
apt-get install openssh-server

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

##### .zshrc (emrah)

```
#bindkey -e
bindkey -v

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
alias vv='vim $(fzf)'
alias cdf='cd $(find . -type d | fzf)'

alias ls='ls --color=auto'
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias .....="cd ../../../.."
alias ......="cd ../../../../.."

source /usr/share/autojump/autojump.sh
source /usr/share/doc/fzf/examples/key-bindings.zsh
```

### packages

#### /etc/apt/sources.list

```
deb http://deb.debian.org/debian/ bookworm main non-free-firmware
deb http://security.debian.org/debian-security bookworm-security main non-free-firmware
deb http://deb.debian.org/debian/ bookworm-updates main non-free-firmware
```

```bash
apt-get update
apt-get install gnupg
apt-get install ack jq unzip
apt-get install git patch
apt-get install net-tools bridge-utils
apt-get install sudo
```

#### /etc/apt/sources.list.d/nodesource.list

```
deb [signed-by=/usr/share/keyrings/nodesource.gpg] https://deb.nodesource.com/node_20.x bookworm main
```

```bash
wget -qO /tmp/nodesource.gpg.key \
  https://deb.nodesource.com/gpgkey/nodesource.gpg.key
cat /tmp/nodesource.gpg.key | gpg --dearmor \
  >/usr/share/keyrings/nodesource.gpg

apt-get update
apt-get install nodejs
npm install npm -g
```

#### /etc/apt/sources.list.d/yarn.list

```
deb [signed-by=/usr/share/keyrings/yarn.gpg] https://dl.yarnpkg.com/debian/ stable main
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
```

```bash
su -l emrah
sudo /usr/bin/systemctl start iwd.service
iwctl
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
apt-get install dnsmasq dns-root-data
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

##### /etc/resolv.conf

```
nameserver 127.0.0.1
nameserver 208.67.222.222
nameserver 8.8.8.8
```

#### /etc/nftables.conf

```
#!/usr/sbin/nft -f

flush ruleset

table inet filter {
  chain input {
    type filter hook input priority 0; policy accept;
  }

  chain forward {
    type filter hook forward priority 0; policy accept;
  }

  chain output {
    type filter hook output priority 0; policy accept;
    iifname "wlan*" ip daddr 172.17.17.0/24 drop
    iifname "enp*" ip daddr 172.17.17.0/24 drop
    iifname "wlan*" ip daddr 172.18.18.0/24 drop
    iifname "enp*" ip daddr 172.18.18.0/24 drop
    #udp dport 10000 drop
    #ip daddr 88.255.123.45 udp dport 10000 drop
  }
}

table ip nat {
  map tcp2ip {
    type inet_service : ipv4_addr
    elements = { 3142 : 172.17.17.10 }
  }

  map tcp2port {
    type inet_service : inet_service
    elements = { 3142 : 3142 }
  }

  map udp2ip {
    type inet_service : ipv4_addr
  }

  map udp2port {
    type inet_service : inet_service
  }

  chain prerouting {
    type nat hook prerouting priority 0; policy accept;
    iifname "wlan*" dnat to tcp dport map @tcp2ip:tcp dport map @tcp2port
    iifname "wlan*" dnat to udp dport map @udp2ip:udp dport map @udp2port
    iifname "enp*" dnat to tcp dport map @tcp2ip:tcp dport map @tcp2port
    iifname "enp*" dnat to udp dport map @udp2ip:udp dport map @udp2port
  }

  chain postrouting {
    type nat hook postrouting priority 100; policy accept;
    ip saddr 172.17.17.0/24 masquerade
    ip saddr 172.18.18.0/24 masquerade
  }

  chain output {
    type nat hook output priority 0; policy accept;
  }

  chain input {
    type nat hook input priority 0; policy accept;
  }
}
```