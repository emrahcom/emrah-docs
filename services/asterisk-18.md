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
allow=ulaw
allow=alaw
allow=vp8
allow=vp9
transport=transport-udp-nat
direct_media=no
rtp_symmetric=yes
force_rport=yes
;ice_support=yes

; auth template
[my-auth](!)
type=auth
auth_type=userpass

; aor template
[my-aor](!)
type=aor
max_contacts=1
remove_existing=true

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
