## Asterisk 18

Tested in `Bookworm` container on `Debian 11 Bullseye` host.

#### installation

```bash
apt-get install asterisk --install-recommends

systemctl status asterisk
asterisk -V
```

#### configuration

##### disable `chan_sip.so`

In `/etc/asterisk/modules.conf`

```conf
noload => chan_sip.so
```

Restart the service:

```bash
systemctl restart asterisk
```
