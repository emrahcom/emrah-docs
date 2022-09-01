## FreePBX

Quick installation using CDROM/USB image.

#### download image

Download `iso` from [freepbx.org](https://www.freepbx.org/downloads/)

#### installation

`virt-manager` is used for this guide.

- copy image into `/var/lib/libvirt/images`
- create a new VM
- local install media
- select `SNG7-PBX...` as image
- Select `CentOS 7` as OS
- 2048 MB RAM / 2 cores
- ~10 GB storage
- properties
  - `name`: _freepbx_
  - `network`: _bridge / br0_
    \
    _depends on your environment_

- Select the recommended\
  FreePBX 16 installation (Asteriks 18)
- Graphical installation - Output to VGA
- FreePBX Standard
- Set `root` password
- reboot

#### system customization

- packages

```bash
yum check-updates
yum install tmux
```

- ssh
  - custom port
  - upload public SSH key

- static IP

**/etc/sysconfig/network-scripts/ifcfg-eth0**

```config
BOOTPROTO="static"
IPADDR=172.17.17.33
NETMASK=255.255.255.0
GATEWAY=172.17.17.1
DNS1=172.17.17.1
```

```bash
systemctl restart network
```

#### FreePBX admin setup

- Go to `https://<FreePBX-IP>`
- Fill required fields
  - `Username`
  - `Password`
  - `Confirm Password`
  - `Notifications Email Address`
  - Click `Setup System` button

#### FreePBX configuration

- Go to `https://<FreePBX-IP>`
- Click `FreePBX Administration`
- Skip activation (_this is only a test setup_)
- Skip, skip, skip...
- Set language
- Disable firewall by clicking `Abort` (_this is only a test setup_)

#### Asterisk Sip Settings

- Click `Settings` -> `Asterisk SIP settings`
- Set `External Address` and `Local Networks` by clicking
  `Detect Network Settings`.
  \
  On my setup:
  - `External IP`: _85.110.x.y_
  - `Local networks`:
    - _192.168.1.0/24_
    - _172.17.17.0/24_
- `Video Support`: _enabled_
- `Submit`

#### links

- https://www.freepbx.org/downloads/
- https://wiki.freepbx.org/display/FPG/Configuring+Your+PBX
