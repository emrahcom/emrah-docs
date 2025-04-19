# Firefox

### Packages

```bash
apt-get install firefox-esr
```

### Tmpfs

/etc/fstab

```
tmpfs  /var/cache/browser  tmpfs  noatime,size=300M,nr_inodes=10k,mode=1777  0  0
```

```bash
mkdir -p /var/cache/browser
mount /var/cache/browser
systemctl daemon-reload
```

### ~/bin/mozilla2disk

```bash
#!/bin/bash

rm -rf ~/archive/browser/mozilla.app
mkdir -p ~/archive/browser/mozilla.app
cp -arp /var/cache/browser/mozilla/* ~/archive/browser/mozilla.app/
```

### ~/bin/mozilla2ram

```bash
#!/bin/bash

rm -rf /var/cache/browser/mozilla
mkdir -p /var/cache/browser/mozilla
cp -arp ~/archive/browser/mozilla.app/* /var/cache/browser/mozilla/

rm -rf /var/cache/browser/mozilla.cache
mkdir -p /var/cache/browser/mozilla.cache
cp -arp ~/archive/browser/mozilla.cache/* /var/cache/browser/mozilla.cache/
```

### Links and permissions

```bash
chmod 700 ~/bin/mozilla2disk ~/bin/mozilla2ram

mkdir -p ~/archive/browser

rm -rf ~/.mozilla
ln -s /var/cache/browser/mozilla ~/.mozilla

rm -rf ~/.cache/mozilla
ln -s /var/cache/browser/mozilla.cache ~/.cache/mozilla
```

### Archive

Copy archive from another machine:

```bash
IP=192.168.1.115

rsync -avhe 'ssh -l emrah' archive/browser ${IP}:~/archive/
```
