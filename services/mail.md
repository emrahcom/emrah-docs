## mail

Mail server on Debian Bullseye

#### DNS

##### PTR record

Use host name as the droplet name on DigitalOcean.\
e.g. `mail.mydomain.corp`

##### A record

Create an `A` record for the mail server.\
e.g. `mail.mydomain.corp`

##### MX record

Create a new `MX` record which points to the mail server. Don't forget the
trailing dot after the host address:

`MX  @  mail.mydomain.corp.  0  600`

##### SPF record

Create a new `TXT` record

`v=spf1 mx -all`

#### links

- [server-world](https://www.server-world.info/en/note?os=Debian_11&p=mail&f=1)
- [SPF, DKIM, DMARC](https://www.linode.com/docs/guides/configure-spf-and-dkim-in-postfix-on-debian-9/)
