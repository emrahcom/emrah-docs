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
apt-get install jq jc
```

##### element-desktop

```bash
wget -O /usr/share/keyrings/riot-im-archive-keyring.gpg \
    https://packages.riot.im/debian/riot-im-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/riot-im-archive-keyring.gpg] \
https://riot.im/packages/debian bullseye main" >> /etc/apt/sources.list

apt-get update
apt-get install element-desktop
```

`~/.spectrwm.conf`

```conf
program[element-desktop]= element-desktop
bind[element-desktop]   = MOD+shift+m
```
