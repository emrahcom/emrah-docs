## libvirt & virt-manager

Tested on `Debian Bookworm`.

### installation

```bash
apt-get install virt-manager --install-recommends
```

### configuration

```bash
adduser my-account libvirt
```

### virt-manager

`ctrl_l + alt_l` are the grap keys.

```bash
virt-manager
```

### Debian guest machine

- bridge `br0`
- only `root`, no normal user

```bash
apt-get install open-vm-tools
```

### links

- https://libvirt.org/
- https://virt-manager.org/
