## Jigasi


### Jitsi sources.list

```bash
apt-get install gnupg

wget -T 30 -qO /tmp/jitsi.gpg.key https://download.jitsi.org/jitsi-key.gpg.key
cat /tmp/jitsi.gpg.key | gpg --dearmor >/usr/share/keyrings/jitsi.gpg
```

_/etc/apt/sources.list.d/jitsi-stable.list_

```
deb [signed-by=/usr/share/keyrings/jitsi.gpg] https://download.jitsi.org stable/
```

```bash
apt-get update
```
