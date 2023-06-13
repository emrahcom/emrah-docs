## Debian Bookworm Installation

#### netinstall

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
