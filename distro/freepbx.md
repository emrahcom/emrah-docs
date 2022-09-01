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

#### links

- https://www.freepbx.org/downloads/
