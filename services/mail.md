## mail

Mail server on Debian Bullseye

#### DNS

##### PTR record

Use host name as droplet name on DigitalOcean.\
e.g. `mail.mydomain.corp`

To check:

```bash
dig -x [IP address]
```

##### A record

Create an `A` record for the mail server.\
e.g. `mail.mydomain.corp`

To check:

```bash
dig mail.mydomain.corp
```

##### MX record

Create a new `MX` record which points to the mail server. Don't forget the
trailing dot after the host address:

`MX  @  mail.mydomain.corp.  0  600`

To check:

```bash
dig MX mydomain.corp
```

##### SPF record

Create a new `TXT` record. Use `@` as host. For some DNS service, the following
value must be quoted. e.g. `"v=spf1 mx -all"`

`v=spf1 mx -all`

To check:

```bash
dig TXT mydomain.corp
```

#### DNS for virtual domains

##### MX record

Create a new `MX` record which points to the mail server. Don't forget the
trailing dot after the host address:

`MX  @  mail.mydomain.corp.  0  600`

To check:

```bash
dig MX virtualdomain.corp
```

##### SPF record

Create a new `TXT` record. Use `@` as host. For some DNS service, the following
value must be quoted. e.g. `"v=spf1 mx -all"`

`v=spf1 mx -all`

To check:

```bash
dig TXT virtualdomain.corp
```

#### postfix

```bash
debconf-set-selections <<< \
    "postfix postfix/main_mailer_type select No configuration"

apt-get -y install postfix sasl2-bin ca-certificates
```

#### links

- [server-world](https://www.server-world.info/en/note?os=Debian_11&p=mail&f=1)
- [SPF, DKIM, DMARC](https://www.linode.com/docs/guides/configure-spf-and-dkim-in-postfix-on-debian-9/)
