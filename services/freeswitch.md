# FreeSwitch

Tested in `Bookworm` container on `Debian 12 Bookworm` host.

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
  "https://freeswitch.signalwire.com/repo/deb/debian-release/ bookworm main" \
  >/etc/apt/sources.list.d/freeswitch.list
apt-get update
```

#### Packages

```bash
apt-get --install-recommends install freeswitch-meta-all
```

## Configuration

#### NAT

- incoming `UDP/5060` and `TCP/5080`
- incoming `TCP/5060` and `TCP/5080`
- incoming `TCP/5061` and `TCP/5081` for TLS
- incoming `UDP/16384-32768`\
  `iif "enp1s0" udp dport 16384-32768 dnat to 172.22.22.18`

#### Default Password

Change the default password.

[/etc/freeswitch/vars.xml](./freeswitch/vars.xml)

```xml
<X-PRE-PROCESS cmd="set" data="default_password=NEW-PASSWORD"/>
```

#### Domain or IP

The default `domain` is the IP of the host. Update the following line in
[/etc/freeswitch/vars.xml](./freeswitch/vars.xml) to set the `domain`.

```xml
<!-- <X-PRE-PROCESS cmd="set" data="domain=$${local_ip_v4}"/> -->
<X-PRE-PROCESS cmd="set" data="domain=sip.mydomain.corp"/>
```

or

```xml
<!-- <X-PRE-PROCESS cmd="set" data="domain=$${local_ip_v4}"/> -->
<X-PRE-PROCESS cmd="set" data="domain=172.17.17.36"/>
```

#### External SIP IP

The default `stun` seems unstable, don't use it for the external environment
too.

For internal test environent, set `host IP` as `external_ip` if `FreeSwitch` is
in the container:

[/etc/freeswitch/vars.xml](./freeswitch/vars.xml)

```xml
<X-PRE-PROCESS cmd="stun-set" data="external_rtp_ip=host:sip.mydomain.corp"/>
<X-PRE-PROCESS cmd="stun-set" data="external_sip_ip=host:sip.mydomain.corp"/>
```

or

```xml
<X-PRE-PROCESS cmd="stun-set" data="external_rtp_ip=172.17.17.36"/>
<X-PRE-PROCESS cmd="stun-set" data="external_sip_ip=172.17.17.36"/>
```

#### Custom RTP ports

In `/etc/freeswitch/autoload_configs/switch.conf.xml`:

```xml
<param name="rtp-start-port" value="10000"/>
<param name="rtp-end-port" value="20000"/>
```

#### Profile domain

In `/etc/freeswitch/sip_profiles/internal.xml`:

```xml
<domains>
  <domain name="$${domain}" parse="true"/>
</domains>
```

See
[Sofia Configuration Files](https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/Configuration/Sofia-SIP-Stack/Sofia-Configuration-Files_7144453/)
for more details.

#### Directory

- Update `/etc/freeswitch/directory/default.xml` to customize groups.
- Update `password` in `/etc/freeswitch/directory/default/*` if needed.

```xml
<param name="password" value="$${default_password}"/>
```

#### Dialplan

- Disabling `voicemail`

`/etc/freeswitch/dialplan/default.xml`

```xml
<extension name="Local_Extension">
  <condition field="destination_number" expression="^(10[01][0-9])$">
    ...
    <action application="set" data="continue_on_fail=false"/>
```

#### Systemd

If `FreeSwitch` starts before `eth0` is up then it listens only the loopback
device and it doesn't work in this case. Don't start its Systemd unit before the
network interface is ready.

_/etc/systemd/system/wait-ifup.service_

```
[Unit]
Description=Wait for the network interface
After=network.target
Before=freeswitch.service

[Service]
User=root
Group=root
ExecStartPre=bash -c "while true; do ping -c1 host.loc && break; sleep 1; done"
ExecStart=true

[Install]
WantedBy=multi-user.target
```

Enable and activate the unit:

```bash
systemctl daemon-reload
systemctl enable wait-ifup.service
systemctl start wait-ifup.service
```

## External Clients

Call `extension@domain:5080` as SIP address. For example:

- `1001@sip.mydomain.corp:5080`
- `1002@1.2.3.4:5080`

It is possible to set `5060` as external SIP port and `5080` as internal SIP
port. So, external clients can call without using SIP port since `5060` is
the default one.

In _/etc/freeswitch/vars.xml_:

```xml
<X-PRE-PROCESS cmd="set" data="internal_sip_port=5080"/>
<X-PRE-PROCESS cmd="set" data="internal_tls_port=5081"/>
...
<X-PRE-PROCESS cmd="set" data="external_sip_port=5060"/>
<X-PRE-PROCESS cmd="set" data="external_tls_port=5061"/>
```

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

## Debug

### sngrep

```bash
apt-get install sngrep
sngrep
```

### sipgrep

```bash
apt-get install sipgrep
```

### loglevel

In `fs_cli`

```
sofia loglevel all 9
```

## Python

In _/etc/freeswitch/autoload_configs/modules.conf.xml_

```xml
<load module="mod_python3"/>
```

```bash
cd /usr/local/lib/python3.11/dist-packages
mkdir -p mypackage
touch mypackage/__init__.py
```

_/usr/local/lib/python3.11/dist-packages/mypackage/mymodule.py_

```python
import freeswitch

def handler(session, args):
    freeswitch.consoleLog("info", "hello1\n")

def fsapi(session, stream, env, args):
    freeswitch.consoleLog("info", "hello2\n")
```

_/etc/freeswitch/dialplan/public/01_myplan.xml_

```xml
<include>
  <extension name="myplan">
    <condition field="destination_number" expression="^(112233)$">
      <action application="set" data="domain_name=$${domain}"/>
      <action application="python" data="mypackage.mymodule"/>
    </condition>
  </extension>
</include>
```

## Links

- https://github.com/signalwire/freeswitch
- https://freeswitch.org/confluence/display/FREESWITCH/Debian
- https://freeswitch.org/confluence/display/FREESWITCH/HOWTO+Create+a+SignalWire+Personal+Access+Token
- https://freeswitch.org/confluence/display/FREESWITCH/mod_conference
- https://github.com/sipcapture/sipgrep
- https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/Client-and-Developer-Interfaces/Lua-API-Reference/
