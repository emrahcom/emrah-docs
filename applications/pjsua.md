## pjsua

### Building

#### Packages

Install packages as `root`:

```bash
apt-get install build-essential
apt-get install libv4l-dev libsdl2-dev libavcodec-dev libavdevice-dev \
  libavfilter-dev libavformat-dev libavutil-dev libswscale-dev libasound2-dev \
  libopus-dev libvpx-dev libssl-dev
```

#### Make

Run the following as a non-root user:

```bash
PJPROJECT_REPO="https://github.com/jitsi-contrib/pjproject"
PJPROJECT_BRANCH="sipjibri"

mkdir -p ~/src
cd ~/src

git clone -b $PJPROJECT_BRANCH $PJPROJECT_REPO
cd pjproject

./configure
make dep
make

cp ~/src/pjproject/pjsip-apps/bin/pjsua-x86_64-unknown-linux-gnu /tmp/pjsua
```

#### Executable

Run the followings as `root`:

```bash
cp /tmp/pjsua /usr/local/bin/pjsua
chmod 755 /usr/local/bin/pjsua
```

### Unencrypted SIP

#### pjsua.default.config

```config
--no-tcp
--video
--auto-update-nat 0
--disable-stun
--dis-codec all
--add-codec pcmu
--add-codec pcma
--add-codec speex
--add-codec G722
--add-codec opus
--no-vad
--ec-tail 0
--quality 10
--max-calls=1
--auto-keyframe=30
--use-cli
--no-cli-console
--no-color
--no-stderr
--log-file=/home/dodo/pjsua/pjsua.log
```

#### Run as server

```bash
pjsua --config-file=./pjsua.default.config --auto-answer=200
```

#### Run as client

```bash
pjsua --config-file=./pjsua.default.config "sip:dodo@172.17.17.33"
```

### SRTP with unencrypted SIP

- `--use-srtp=N`
  - `0`: disabled
  - `1`: optional
  - `2`: mandatory

- `--srtp-secure=N`
  - `0`: no
  - `1`: tls
  - `2`: sips

#### pjsua.srtp.config

```config
--use-srtp=2
--srtp-secure=0
--no-tcp
--video
--auto-update-nat 0
--disable-stun
--dis-codec all
--add-codec pcmu
--add-codec pcma
--add-codec speex
--add-codec G722
--add-codec opus
--no-vad
--ec-tail 0
--quality 10
--max-calls=1
--auto-keyframe=30
--use-cli
--no-cli-console
--no-color
--no-stderr
--log-file=/home/dodo/pjsua/pjsua.log
```

#### Run as server

```bash
pjsua --config-file=./pjsua.srtp.config --auto-answer=200
```

#### Run as client

```bash
pjsua --config-file=./pjsua.srtp.config "sip:dodo@172.17.17.33"
```

### SRTP with encrypted SIP

#### TLS certificates

```bash
mkdir tls
cd tls

TAG=dodo
APP=pjsua
CN=172.17.17.33

openssl req -nodes -new -x509 -days 10950 \
  -keyout $TAG-CA.key -out $TAG-CA.pem \
  -subj "/O=$TAG/OU=CA/CN=$TAG $DATE-$RANDOM"
openssl req -nodes -newkey rsa:2048 \
  -keyout $TAG-$APP.key -out $TAG-$APP.csr \
  -subj "/O=$TAG/OU=$TAG-$APP/CN=$CN"
openssl x509 -req -CA $TAG-CA.pem -CAkey $TAG-CA.key \
  -CAcreateserial -days 10950 \
  -in $TAG-$APP.csr -out $TAG-$APP.pem
```

#### pjsua.tls.config

- The order of `--use-tls`, `--no-udp` and `--no-tcp` is important.

- Both sides (_server and client_) should provide certificates.

- Certificates are not validated by default. Use `--tls-verify-client` and
  `--tls-verify-server` to validate certificates.

- Use trusted certificates or provide CA certificate with `--tls-ca-file` from
  which the certificates are generated.

```config
--use-srtp=2
--srtp-secure=1
--use-tls
--no-udp
--no-tcp
--tls-ca-file tls/dodo-CA.pem
--tls-cert-file tls/dodo-pjsua.pem
--tls-privkey-file tls/dodo-pjsua.key
--tls-verify-client
--tls-verify-server
--video
--auto-update-nat 0
--disable-stun
--dis-codec all
--add-codec pcmu
--add-codec pcma
--add-codec speex
--add-codec G722
--add-codec opus
--no-vad
--ec-tail 0
--quality 10
--max-calls=1
--auto-keyframe=30
--use-cli
--no-cli-console
--no-color
--no-stderr
--log-file=/home/dodo/pjsua/pjsua.log
```

#### Run as server

```bash
pjsua --config-file=./pjsua.tls.config --auto-answer=200
```

#### Run as client

```bash
pjsua --config-file=./pjsua.tls.config \
  "sip:dodo@172.17.17.33:5061;transport=tls"
```

### References

- [pjsua](https://www.pjsip.org/pjsua.htm)
- [SRTP](https://docs.pjsip.org/en/latest/specific-guides/security/srtp.html)
- [TLS](https://docs.pjsip.org/en/latest/specific-guides/security/ssl.html)
