## Asterisk

Tested on `Debian 11 Bullseye`

#### installation

```bash
apt-get install asterisk asterisk-dahdi

systemctl status asterisk
asterisk -V
```

#### sip.conf

```config
[general]
context=default

[1001]
type=friend
context=from-internal
host=dynamic
secret=1001
disallow=all
allow=ulaw

[1002]
type=friend
context=from-internal
host=dynamic
secret=1002
disallow=all
allow=ulaw
```

#### links

- https://www.how2shout.com/linux/how-to-install-asterisk-voip-server-on-debian-11-10/
