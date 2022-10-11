## FreeSwitch

Tested in `Bullseye` container on `Debian 11 Bullseye` host.

### installation

##### nat

- incoming `UDP/5060`
- incoming `UDP/10000-20000`
  \
  `iif "enp1s0" udp dport 10000-20000 dnat to 172.22.22.18`

##### links
