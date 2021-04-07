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
