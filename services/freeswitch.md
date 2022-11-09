# FreeSwitch

Tested in `Bullseye` container on `Debian 11 Bullseye` host.

## Installation

#### Access Token

- create an account on [SignalWire](https://id.signalwire.com/)
- `profile` -> `personal access tokens` -> `new token`
- keep the generated token in a safe place

#### Repo

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

#### Packages

```bash
apt-get --install-recommends install freeswitch-meta-all
```

## Configuration

#### NAT

- incoming `UDP/5060`
- incoming `UDP/16384-32768`
  \
  `iif "enp1s0" udp dport 16384-32768 dnat to 172.22.22.18`

#### Default Password

Change the default password.

[/etc/freeswitch/vars.xml](./freeswitch/vars.xml)

```xml
<X-PRE-PROCESS cmd="set" data="default_password=NEW-PASSWORD"/>
```

#### Domain or IP

Don't update `domain` in [/etc/freeswitch/vars.xml](./freeswitch/vars.xml). This
is only for info.

```xml
<X-PRE-PROCESS cmd="set" data="domain=$${local_ip_v4}"/>
<X-PRE-PROCESS cmd="set" data="domain=freeswitch.mydomain.corp"/>
```

For multi-tenant system, comment followings in
[/etc/freeswitch/sip_profiles/internal.xml](./freeswitch/sip_profiles/internal.xml)

```xml
<!-- <param name="force-register-domain" value="$${domain}"/> -->
<!-- <param name="force-subscription-domain" value="$${domain}"/> -->
<!-- <param name="force-register-db-domain" value="$${domain}"/> -->
```

#### External SIP IP

For internal test environent, set `host IP` as `external_ip` if `FreeSwitch` is
in the container:

[/etc/freeswitch/vars.xml](./freeswitch/vars.xml)

```xml
<X-PRE-PROCESS cmd="stun-set" data="external_rtp_ip=172.17.17.36"/>
<X-PRE-PROCESS cmd="stun-set" data="external_sip_ip=172.17.17.36"/>
```

#### Directory

See [/etc/freeswitch/directory/](./freeswitch/directory/) for a sample.

#### Dialplan

- Disable voicemail

```xml
<extension name="Local_Extension">
  <condition field="destination_number" expression="^(10[01][0-9])$">
    ...
    <action application="set" data="continue_on_fail=false"/>
```

See [/etc/freeswitch/dialplan/](./freeswitch/dialplan/) for a sample.

## Testing

- `9195`: _instant echo_
- `9196`: _delayed echo_
- `9664`: _hold music_
- `9193`: _record video_
- `9194`: _play recorded video_
- `9001`: _conference_

## FreeSwitch CLI

```bash
fs_cli
```

- `help`
- `show <tab>`
- `show registrations`

## Links

- https://github.com/signalwire/freeswitch
- https://freeswitch.org/confluence/display/FREESWITCH/Debian
- https://freeswitch.org/confluence/display/FREESWITCH/HOWTO+Create+a+SignalWire+Personal+Access+Token
- https://freeswitch.org/confluence/display/FREESWITCH/mod_conference
