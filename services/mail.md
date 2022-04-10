## mail server

Mail server on Debian Bullseye

#### Ports

- `25/TCP` SMTP
- `110/TCP` POP3
- `143/TCP` IMAP
- `993/TCP` IMAPS
- `995/TCP` POP3S

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

#### certbot

##### lxc

If it's in a container

```bash
mkdir -p /var/lib/lxc/mail/rootfs/var/www/html
```

_/var/lib/lxc/mail/config_

```conf
lxc.mount.entry = /var/www/html var/www/html none bind 0 0
```

##### packages

```bash
apt-get --install-recommends install certbot
```

##### config

```bash
FQDN=mail.mydomain.corp

certbot certonly --dry-run --non-interactive -m info@$FQDN --agree-tos \
    --duplicate --webroot -w /var/www/html -d $FQDN
certbot certonly --non-interactive -m info@$FQDN --agree-tos \
    --duplicate --webroot -w /var/www/html -d $FQDN

find /etc/letsencrypt/archive -name 'privkey*.pem' -exec chmod 640 {} \;
chmod 750 /etc/letsencrypt/{archive,live}
chown root:ssl-cert /etc/letsencrypt/{archive,live} -R
```

#### postfix

##### packages

```bash
debconf-set-selections <<< \
    "postfix postfix/main_mailer_type select No configuration"

apt-get -y --no-install-recommends install postfix sasl2-bin ca-certificates
```

##### config

```bash
cp /usr/share/postfix/main.cf.dist /etc/postfix/main.cf
```

_/etc/postfix/main.cf_

`myhostname` and `mydomain` will be updated according to actual values.

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

##### restart

#### dovecot

##### packages

```bash
newaliases
systemctl restart postfix.service
```

```bash
apt-get -y --no-install-recommends install dovecot-core dovecot-pop3d \
    dovecot-imapd
```

##### config

_/etc/dovecot/dovecot.conf_

```conf
!include_try /usr/share/dovecot/protocols.d/*.protocol
listen = *
dict {
}
!include conf.d/*.conf
!include_try local.conf
```

_/etc/dovecot/conf.d/10-auth.conf_

```conf
disable_plaintext_auth = no
auth_mechanisms = plain login
!include auth-system.conf.ext
```

_/etc/dovecot/conf.d/10-mail.conf_

```conf
mail_location = maildir:~/Maildir
namespace inbox {
  inbox = yes
}
mail_privileged_group = mail
protocol !indexer-worker {
}
```

_/etc/dovecot/conf.d/10-master.conf_

```conf
service imap-login {
  inet_listener imap {
    #port = 143
  }
  inet_listener imaps {
    #port = 993
    #ssl = yes
  }
}

service pop3-login {
  inet_listener pop3 {
    #port = 110
  }
  inet_listener pop3s {
    #port = 995
    #ssl = yes
  }
}

service submission-login {
  inet_listener submission {
    #port = 587
  }
}

service lmtp {
  unix_listener lmtp {
    #mode = 0666
  }
}

service imap {
}

service pop3 {
}

service submission {
}

service auth {
  unix_listener auth-userdb {
  }

  unix_listener /var/spool/postfix/private/auth {
    mode = 0666
    user = postfix
    group = postfix
  }
}

service auth-worker {
}

service dict {
  unix_listener dict {
  }
}
```

##### restart

```bash
systemctl restart dovecot.service
```

#### links

- [server-world](https://www.server-world.info/en/note?os=Debian_11&p=mail&f=1)
- [SPF, DKIM, DMARC](https://www.linode.com/docs/guides/configure-spf-and-dkim-in-postfix-on-debian-9/)
