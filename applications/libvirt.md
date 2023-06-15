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
- ssh

_/etc/ssh/sshd_config.d/emrah.conf_

```
Port 22
```

```bash
cd /tmp
wget https://emrah.com/files/emrah.pub
cp emrah.pub /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys
systemctl restart ssh
```

```bash
apt-get install open-vm-tools
```

### links

- https://libvirt.org/
- https://virt-manager.org/
