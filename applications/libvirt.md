## libvirt & virt-manager

Tested on `Debian Bookworm`.

### installation

```bash
apt-get install virt-manager --install-recommends
```

For VM:

```bash
apt-get install virt-manager --no-install-recommends
apt-get install libvirt-daemon-system libvirt-clients
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

For a better result, run the following commands inside VM before shrinking:

```bash
dd if=/dev/zero of=/zero.file bs=1M status=progress
rm /zero.file
sync
poweroff
```

`-c` is an optional flag for compressing. Run without `-c` for a quicker but
less aggresive reducing:

```bash
cd /var/lib/libvirt/images

qemu-img convert -c -O qcow2 old.qcow2 new.qcow2
mv new.qcow2 old.qcow2
```

### Audio

Run VMs with the user account:

/etc/libvirt/qemu.conf

```
user = "emrah"
group = "emrah"
```

Restart the service:

```bash
systemctl restart libvirtd.service
systemctl is-active libvirtd.service
```

Permissions:

```bash
mkdir -p /etc/apparmor.d/local/abstractions
```

/etc/apparmor.d/local/abstractions/libvirt-qemu

```
/usr/share/pipewire/** r,
/etc/pipewire/** r,
/home/emrah/.config/pipewire/** r,
/usr/lib/@{multiarch}/spa-0.2/** mr,
/usr/lib/@{multiarch}/pipewire-0.3/** mr,
/run/user/1000/ r,
/run/user/1000/pipewire-[0-9]* rw,
/run/user/1000/pipewire-[0-9]*-manager rw,
```

```bash
systemctl reload apparmor
```

Per VM:

```bash
virsh --connect qemu:///system edit <VM name>
```

Keep the address:

```
<sound model='ich9'>
  <audio id='1'/>
</sound>
<audio id='1' type='pipewire' runtimeDir='/run/user/1000'/>
```

Restart the VM and connect:

```bash
apt-get install alsa-utils
adduser emrah audio
```

Test with the user account:

```bash
arecord -f cd -d 5 /tmp/t.wav
aplay /tmp/t.wav
```

### links

- https://libvirt.org/
- https://virt-manager.org/
