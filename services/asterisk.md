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
allow=vp8
videosupport=yes

[1002]
type=friend
context=from-internal
host=dynamic
secret=1002
disallow=all
allow=ulaw
allow=vp8
videosupport=yes

[8888]
type=friend
context=from-internal
host=dynamic
secret=8888
disallow=all
allow=ulaw
allow=vp8
videosupport=yes
```

#### extensions.conf

```config
[from-internal]

exten => 1001,1,Dial(SIP/1001,20)
exten => 1002,1,Dial(SIP/1002,20)
exten => 8888,1,Dial(SIP/8888,20)

exten => 1000,1,Answer()
same = n,Wait(1)
same = n,Playback(hello-world)
same = n, Hangup()
```

#### SIP traffic

```bash
ngrep -q "." port 5060
```

#### links

- https://www.how2shout.com/linux/how-to-install-asterisk-voip-server-on-debian-11-10/
- https://github.com/antonraharja/book-asterisk-101
