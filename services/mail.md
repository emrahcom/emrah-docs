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

##### packages

```bash
debconf-set-selections <<< \
    "postfix postfix/main_mailer_type select No configuration"

apt-get -y install postfix sasl2-bin ca-certificates
```

##### config

```bash
cp /usr/share/postfix/main.cf.dist /etc/postfix/main.cf

`myhostname` and `mydomain` will be updated according to actual values.
```

_/etc/postfix/main.cf_

```conf
compatibility_level = 2
command_directory = /usr/sbin
daemon_directory = /usr/lib/postfix/sbin
data_directory = /var/lib/postfix
mail_owner = postfix
myhostname = mail.mydomain.corp
mydomain = mydomain.corp
myorigin = $mydomain
inet_interfaces = all
mydestination = $myhostname, localhost.$mydomain, localhost, $mydomain
local_recipient_maps = unix:passwd.byname $alias_maps
unknown_local_recipient_reject_code = 550
#mynetworks_style = subnet (if it is in an isolated network)
mynetworks_style = host
#mynetworks = 127.0.0.0/8, 172.22.22.0/24
mynetworks = 127.0.0.0/8
alias_maps = hash:/etc/aliases
alias_database = hash:/etc/aliases
home_mailbox = Maildir/
smtpd_banner = $myhostname ESMTP
debugger_command =
         PATH=/bin:/usr/bin:/usr/local/bin:/usr/X11R6/bin
         ddd $daemon_directory/$process_name $process_id & sleep 5
sendmail_path = /usr/sbin/postfix
newaliases_path = /usr/bin/newaliases
mailq_path = /usr/bin/mailq
setgid_group = postdrop
# html_directory =
# manpage_directory =
# sample_directory =
# readme_directory =
inet_protocols = ipv4

# additional settings
disable_vrfy_command = yes
smtpd_helo_required = yes
message_size_limit = 1024000

# SMTP-Auth settings
smtpd_sasl_type = dovecot
smtpd_sasl_path = private/auth
smtpd_sasl_auth_enable = yes
smtpd_sasl_security_options = noanonymous
smtpd_sasl_local_domain = $myhostname
smtpd_recipient_restrictions = permit_mynetworks, permit_auth_destination,
permit_sasl_authenticated, reject
```

#### links

- [server-world](https://www.server-world.info/en/note?os=Debian_11&p=mail&f=1)
- [SPF, DKIM, DMARC](https://www.linode.com/docs/guides/configure-spf-and-dkim-in-postfix-on-debian-9/)
