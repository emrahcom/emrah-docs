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

### Files

Machines are in `/etc/libvirt/qemu/`.
Images are in `/etc/libvirt/qemu/images/`.

### Debian guest machine

- bridge `br0`
- only `root`, no normal user
- /etc/ssh/sshd_config.d/emrah.conf

```
Port 22
```

- /etc/apt/apt.conf

```
Acquire::http::Proxy "http://172.17.17.10:3142/";
```

- /etc/apt/apt.conf.d/80recommends

```
APT::Install-Recommends "0";
APT::Install-Suggests "0";
```

- /etc/default/grub

```
GRUB_TIMEOUT=1
```

- initial commands

```bash
update-grub

cd /tmp
wget https://emrah.com/files/emrah.pub
cp emrah.pub /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys
systemctl restart ssh

apt-get update
apt-get install zsh tmux vim autojump fzf
apt-get install open-vm-tools
apt-get install ack net-tools
apt-get purge installation-report reportbug nano
apt-get purge os-prober
apt-get autoremove --purge

chsh -s /bin/zsh root
```

- rc files
  - .bashrc
  - .tmux.conf
  - .zshrc
  - .vimrc

- last commands

```bash
apt-get update && apt-get autoclean && apt-get dist-upgrade -dy && \
  apt-get dist-upgrade && apt-get autoremove --purge
poweroff
```

### Shrink

```bash
cd /var/lib/libvirt/images

qemu-img convert -c -O qcow2 old.qcow2 new.qcow2
mv new.qcow2 old.qcow2
```

### links

- https://libvirt.org/
- https://virt-manager.org/
