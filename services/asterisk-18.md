## Asterisk 18

Tested in `Bookworm` container on `Debian 11 Bullseye` host.

#### installation

```bash
apt-get install asterisk --install-recommends

systemctl status asterisk
asterisk -V
```

#### configuration

- disable `chan_sip.so`
  \
  in `/etc/asterisk/modules.conf`

```conf
noload => chan_sip.so
```

```bash
systemctl restart asterisk
```
