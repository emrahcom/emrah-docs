## pjsua

### pjsua.config

```config
--video
--no-color
--log-level=5
--app-log-level=5
--auto-update-nat 0
--disable-stun
--no-tcp
--dis-codec GSM
--dis-codec H263
--dis-codec iLBC
--dis-codec G722
--dis-codec speex
--dis-codec pcmu
--dis-codec pcma
--dis-codec opus
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
--no-stderr
--log-file=/home/dodo/pjsua/pjsua.log
```

### Run as server

```bash
pjsua --config-file=./pjsua.config --auto-answer=200
```

### Run as client

```bash
pjsua --config-file=./pjsua.config "sip:dodo@172.17.17.33"
```

### TLS certificates

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

### SIP over TLS

Server

```bash
pjsua --config-file=./pjsua.config --use-tls \
  --tls-ca-file tls/dodo-CA.pem --tls-cert-file tls/dodo-pjsua.pem \
  --tls-privkey-file tls/dodo-pjsua.key --auto-answer=200
```

Client:

```bash
pjsua --config-file=./pjsua.config --use-tls \
  "sip:dodo@172.17.17.33;transport=tls"
```

### References

- [pjsua](https://www.pjsip.org/pjsua.htm)
- [SRTP](https://docs.pjsip.org/en/latest/specific-guides/security/srtp.html)
- [TLS](https://docs.pjsip.org/en/latest/specific-guides/security/ssl.html)
