## FreeSwitch

Tested in `Bullseye` container on `Debian 11 Bullseye` host.

### installation

##### access token

- create an account on (SignalWire)[https://id.signalwire.com/]
- `profile` -> `personal access tokens` -> `new token`
- keep the generated token in a safe place

##### repo

```bash
apt-get update
apt-get install gnupg wget

TOKEN=<the-access-token>
echo "machine freeswitch.signalwire.com login signalwire password $TOKEN" \
  >/etc/apt/auth.conf
chmod 600 /etc/apt/auth.conf

wget --http-user=signalwire --http-password=$TOKEN \
  -O /usr/share/keyrings/freeswitch.gpg \
  https://freeswitch.signalwire.com/repo/deb/debian-release/signalwire-freeswitch-repo.gpg

echo "deb [signed-by=/usr/share/keyrings/freeswitch.gpg]" \
  "https://freeswitch.signalwire.com/repo/deb/debian-release/ bullseye main" \
  >/etc/apt/sources.list.d/freeswitch.list
apt-get update
```

##### packages

```bash
apt-get --install-recommends install freeswitch-meta-all
```

##### nat

- incoming `UDP/5060`
- incoming `UDP/10000-20000`
  \
  `iif "enp1s0" udp dport 10000-20000 dnat to 172.22.22.18`

##### links

- https://github.com/signalwire/freeswitch
- https://freeswitch.org/confluence/display/FREESWITCH/Debian
- https://freeswitch.org/confluence/display/FREESWITCH/HOWTO+Create+a+SignalWire+Personal+Access+Token
