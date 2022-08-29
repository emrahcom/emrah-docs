## Jitsi

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