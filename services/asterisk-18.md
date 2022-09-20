## Asterisk 18

Tested in `Bookworm` container on `Debian 11 Bullseye` host.

### installation

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
external_media_address=172.17.17.18
external_signaling_address=172.17.17.18
```
