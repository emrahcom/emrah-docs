## Asterisk 18

Tested in `Bookworm` container on `Debian 11 Bullseye` host.

### installation

##### nat

- incoming `UDP/5060`
- incoming `UDP/10000-20000`
  \
  `iif "enp1s0" udp dport 10000-20000 dnat to 172.22.22.18`

##### freeradius-utils

```bash
apt-get install freeradius-utils --install-recommends
ln -s radcli /etc/radiusclient-ng
```

##### asterisk

```bash
apt-get install asterisk --install-recommends

systemctl status asterisk
asterisk -V
```

##### tools

```bash
apt-get install sngrep ngrep
```

### configuration

##### disable `chan_sip.so` module

In `/etc/asterisk/modules.conf`

```conf
noload => chan_sip.so
```

Restart the service:

```bash
systemctl restart asterisk
```

##### pjsip.conf

```conf
[transport-udp-nat]
type=transport
protocol=udp
bind=0.0.0.0
local_net=172.22.22.0/24
external_media_address=172.17.17.35
external_signaling_address=172.17.17.35

; endpoint template
[my-endpoint](!)
type=endpoint
context=phones
disallow=all
allow=opus
allow=ulaw
allow=alaw
allow=h264
allow=vp8
allow=vp9
transport=transport-udp-nat
direct_media=no
rtp_keepalive=5
rtp_timeout=15
rtp_timeout_hold=15
rtp_symmetric=yes
force_rport=yes
rewrite_contact=yes
;ice_support=yes
device_state_busy_at=1

; auth template
[my-auth](!)
type=auth
auth_type=userpass

; aor template
[my-aor](!)
type=aor
max_contacts=1
remove_existing=true
qualify_frequency=60
qualify_timeout=3.0

[1001](my-endpoint)
auth=1001
aors=1001

[1001](my-auth)
username=1001
password=pwd1001

[1001](my-aor)

[1002](my-endpoint)
auth=1002
aors=1002

[1002](my-auth)
username=1002
password=pwd1002

[1002](my-aor)
```

```bash
systemctl restart asterisk

asterisk -r
CLI> pjsip list endpoints
CLI> pjsip list auths
CLI> pjsip list aors

CLI> pjsip show endpoint 1001
CLI> pjsip show auth 1001
CLI> pjsip show aor 1001
```

##### extensions.conf

```conf
[phones]
exten => 1001,1,Verbose(3,${EXTEN})
 same => n,Dial(PJSIP/1001,20)
 same => n,Playtones(congestion)
 same => n,Congestion(3)
 same => n,HangUp()

exten => 1002,1,Verbose(3,${EXTEN})
 same => n,Dial(PJSIP/1002,20)
 same => n,Playtones(congestion)
 same => n,Congestion(3)
 same => n,HangUp()
```

### Links

[How to install Asterisk](https://www.youtube.com/watch?v=Qt0KLR8K9MY)
