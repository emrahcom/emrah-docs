## Asterisk 16

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

; jitsi
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

; auto answer
exten => 1000,1,Answer()
same = n,Wait(1)
same = n,Playback(hello-world)
same = n, Hangup()

; users
exten => 1001,1,Dial(SIP/1001,20)
exten => 1002,1,Dial(SIP/1002,20)

; jitsi
exten => 8888,1,Dial(SIP/8888,20)

; conference room for guest
exten => 8000,1,Progress()
exten => 8000,2,Wait(1)
exten => 8000,3,ConfBridge(1,default_bridge,default_user)

; conference room for admin
exten => 8001,1,Progress()
exten => 8001,2,Wait(1)
exten => 8001,3,ConfBridge(1,default_bridge,admin_user)
```

#### confbridge.conf

```config
[general]

[admin_user]
type=user
pin=8001
marked=yes
admin=yes
music_on_hold_when_empty=yes

[default_user]
type=user
wait_marked=yes
end_marked=yes
music_on_hold_when_empty=yes
announce_user_count=yes

[default_bridge]
type=bridge
max_members=10
```

#### SIP traffic

```bash
ngrep -q "." port 5060
```

#### links

- https://www.how2shout.com/linux/how-to-install-asterisk-voip-server-on-debian-11-10/
- https://github.com/antonraharja/book-asterisk-101
- https://damow.net/dynamic-conferences-with-asterisk/
