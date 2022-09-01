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
- ~20 GB storage
- properties
  - name: freepbx
  - network: bridge / br0 (depends on your environment)

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

  _/etc/sysconfig/network-scripts/ifcfg-eth0_

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

#### links

- https://www.freepbx.org/downloads/
