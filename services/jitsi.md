## Jitsi

#### Docker-Compose

Download
[the lastest stable](https://github.com/jitsi/docker-jitsi-meet/releases):

```bash
ARCHIVE="https://github.com/jitsi/docker-jitsi-meet/archive/refs/tags"
wget $ARCHIVE/stable-8319.tar.gz
```

Extract:

```bash
tar xzf stable-8319.tar.gz
```

Create `env` and customize it:

```bash
cd docker-jitsi-meet-stable-8319
cp env.example .env
```

Create local directories:

```bash
mkdir -p ~/.jitsi-meet-cfg/{web,transcripts,prosody/config}
mkdir -p ~/.jitsi-meet-cfg/{prosody/prosody-plugins-custom,jicofo,jvb}
mkdir -p ~/.jitsi-meet-cfg/{jigasi,jibri}
```

#### Multiple local pairs for `jvb`

```bash
# don't disable STUN in sip-communicator.properties
hocon -f /etc/jitsi/videobridge/jvb.conf set \
  ice4j.harvest.mapping.stun.enabled true

# first local pair
hocon -f /etc/jitsi/videobridge/jvb.conf set \
  ice4j.harvest.mapping.static-mappings.0.local-address 172.22.22.14
hocon -f /etc/jitsi/videobridge/jvb.conf set \
  ice4j.harvest.mapping.static-mappings.0.public-address 192.168.1.56

# second local pair
hocon -f /etc/jitsi/videobridge/jvb.conf set \
  ice4j.harvest.mapping.static-mappings.1.local-address 172.22.22.14
hocon -f /etc/jitsi/videobridge/jvb.conf set \
  ice4j.harvest.mapping.static-mappings.1.public-address 10.1.1.56

systemctl restart jitsi-videobridge2.service
```
