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

Copy archive from another machine if there is already a customized setup:

```bash
IP=192.168.1.115

rsync -avhe 'ssh -l emrah' archive/browser ${IP}:~/archive/
```

### Customizations

#### Settings

- General -> Make default
- General -> Tabs -> Confirm before quitting with Ctrl+Q: Off
- General -> Language -> Check your spelling as you type: Off
- General -> Downloads -> Always ask you where to save files: On
- General -> Applications -> Ask whether to open or save files: Selected
- General -> Browsing -> Recommend extensions as you browse: Off
- General -> Browsing -> Recommend features as you browse: Off
- General -> Network Proxy -> Settings
  - Manual Proxy Configuration
  - SOCKS Host: localhost
  - SOCKS Port: 65022
  - SOCKS Type: SOCKS v5
  - No Proxy for: localhost, 127.0.0.1, 192.168.0.0/16, 172.16.0.0/12,
    10.0.0.0/8
  - Proxy DNS when using SOCKS v5: true
- Home -> Homepage and new windows: Custom URLS (https://emrah.com/)
- Home -> New tabs: Blank Page
- Home -> Firefox Home Content -> All disabled
- Search -> Default Search Engine: DuckDuckGo
- Search -> Search Suggestions -> Show search suggestions: Off
- Search -> Search Suggestions -> Show recent searches
- Search -> Address Bar -> All disabled
- Privacy & Security -> Content Blocking -> Strict
- Privacy & Security -> Cookies and Site Data -> Delete cookies and site data
  when Firefox is closed: On
- Privacy & Security -> Passwords -> Ask to save passwords: Off
- Privacy & Security -> History -> Clear history when Firefox closes
- Privacy & Security -> Firefox Data Collection and Use -> All disabled
- Privacy & Security -> Security -> Block dangerous and deceptive content: Off
- Privacy & Security -> Certificates -> View Certificates -> Authorities ->
  Delete or Distrust
  - E-Tuğra (silinecek)
  - TUBITAK (silinecek)
  - TURKTRUST (silinecek)

#### about:config

- browser.cache.disk.enable: false
- browser.sessionstore.interval: 60000
- network.prefetch-next: false

#### Topbar & menu

- Bookmarks toolbar -> Never show: Selected

#### Add-ons

- Tridactyl
- uBlock Origin
- Privacy Badger
- NoScript Security Suite by Giorgio Maone
  - NoScript options -> Per-site permissions -> Clear all
  - Add sites by visiting manually
    - emrah.com
