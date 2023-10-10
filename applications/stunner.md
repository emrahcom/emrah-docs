# Stunner

## Installation

https://github.com/firefart/stunner/releases/

```bash
cd ~/downloads
wget https://github.com/firefart/stunner/releases/download/v0.5.3/stunner_0.5.3_Linux_x86_64.tar.gz

cp stunner_0.5.3_Linux_x86_64.tar.gz /tmp/
cd /tmp
tar zxf stunner_0.5.3_Linux_x86_64.tar.gz
cp stunner ~/bin/
```

## Usage

```bash
stunner info -s turn.mydomain.corp:443 --protocol tcp --tls
```

## Secret to credential

```bash
SECRET=CMls74cXjtkwBoSx
EPOCH=$(date +%s)
EXPIRY=8400
TURN_USERNAME=$(( $EPOCH + $EXPIRY ))
TURN_PASSWORD=$(echo -n $USERNAME | openssl dgst -binary -sha1 -hmac $SECRET | \
    openssl base64)
```
