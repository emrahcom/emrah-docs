## iwd

iNet wireless daemon

#### installation

```bash
apt-get purge wpasupplicant
apt-get autoremove --purge

apt-get install iwd
```

#### iwctl

```bash
iwctl
  help
  device list
  station <device> scan
  station <device> get-networks
  station <device> connect <ssid>
  station <device> disconnect

  known-networks list
  known-networks <ssid> forget
```

#### interfaces

**/etc/network/interfaces**

```conf
allow-hotplug wlan0
iface wlan0 inet dhcp
```

#### systemd

```bash
systemctl enable iwd
systemctl restart iwd
```

#### config

```bash
ls /var/lib/iwd/
```

#### links

- [iwd wiki](https://iwd.wiki.kernel.org/)
- [archlinux wiki](https://wiki.archlinux.org/index.php/Iwd)
