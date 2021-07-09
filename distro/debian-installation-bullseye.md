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

#### element-desktop

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
