## Jigasi


### Packages

```bash
apt-get install gnupg
apt-get install openjdk-11-jre-headless
```

### Jitsi sources.list

```bash
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

### Jigasi installation

```bash
SIP_ACCOUNT="1000@sip.mydomain.corp"
SIP_PASSWD="mysecret"
JITSI_FQDN="jitsi.mydomain.corp"

debconf-set-selections <<< \
    "jigasi jigasi/sip-account string $SIP_ACCOUNT"
debconf-set-selections <<< \
    "jigasi jigasi/sip-password password $SIP_PASSWD"
debconf-set-selections <<< \
    "jigasi jitsi-videobridge/jvb-hostname string $JITSI_FQDN"

apt-get install --instal-recommends jigasi
```
