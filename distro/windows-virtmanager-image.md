## Windows on Virt-Manager

This guide explains how to deploy `Free Windows 10` on `Virt-Manager`. This is a
completely legal action but the virtual machine expires after 90 days.

#### Image download

- Go to
  [Virtual Machines](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/).

- Select `MSEdge on Win10 (x64) Stable` as virtual machine.

- Select `VirtualBox` as VM platform.

- Click `Download zip`.

#### Convert image

```bash
unzip MSEdge.Win10.VirtualBox.zip
tar -xvf 'MSEdge - Win10.ova'

qemu-img convert -O qcow2 'MSEdge - Win10-disk001.vmdk' windows-$(date +'%Y%m%d').qcow2
```

#### Put image into archive

Run as `root`

```bash
mv windows-$(date +'%Y%m%d').qcow2 /var/lib/libvirt/
```

#### Create virtual machine

- Import existing disk image

- `Microsoft Windows 10` as OS
