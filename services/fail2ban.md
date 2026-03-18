# fail2ban

Tested on Debian 13 Trixie.

## Installation

```bash
apt-get install fail2ban
```

## Postfix and Dovecot

Install `rsyslog` in the mail container. So, `/var/log/mail/log` will be
created.

_/etc/fail2ban/jail.d/defaults-debian.conf_

```
[DEFAULT]
banaction = nftables
banaction_allports = nftables[type=allports]

[sshd]
backend = systemd
journalmatch = _SYSTEMD_UNIT=ssh.service + _COMM=sshd
enabled = true
maxretry = 3
findtime = 1h
bantime = 24h
action = nftables[port="22", blocktype=drop]
```

_/etc/fail2ban/jail.d/mycustom.conf_

```
[DEFAULT]
ignoreip = 127.0.0.1/8 1.2.3.4

[postfix-sasl]
enabled = true
backend = auto
logpath = /var/lib/lxc/mail/rootfs/var/log/mail.log
maxretry = 3
findtime = 24h
bantime = 24h
action = nftables[table_family=ip, port="25,143,465,587", chain_type=nat, chain_hook=prerouting, chain_priority=-2, blocktype=drop]

[dovecot]
enabled = true
backend = auto
logpath = /var/lib/lxc/mail/rootfs/var/log/mail.log
maxretry = 3
findtime = 24h
bantime = 24h
action = nftables[table_family=ip, port="25,143,465,587", chain_type=nat, chain_hook=prerouting, chain_priority=-2, blocktype=drop]
```

Restart `fail2ban`

```bash
systemctl restart fail2ban
```

## Monitoring

```bash
nft list ruleset

tail -f /var/log/fail2ban.log
```
