## FreeSwitch

Tested in `Bullseye` container on `Debian 11 Bullseye` host.

### installation

##### access token

- create an account on (SignalWire)[https://id.signalwire.com/]
- `profile` -> `personal access tokens` -> `new token`
- keep the generated token in a safe place

##### nat

- incoming `UDP/5060`
- incoming `UDP/10000-20000`
  \
  `iif "enp1s0" udp dport 10000-20000 dnat to 172.22.22.18`

##### links

- https://github.com/signalwire/freeswitch
- https://freeswitch.org/confluence/display/FREESWITCH/Debian
- https://freeswitch.org/confluence/display/FREESWITCH/HOWTO+Create+a+SignalWire+Personal+Access+Token
