# yarn

Tested on `Debian 11 Bullseye`

### packages

run as `root`

```bash
wget -qO /tmp/yarn.gpg.key https://dl.yarnpkg.com/debian/pubkey.gpg
cat /tmp/yarn.gpg.key | gpg --dearmor >/usr/share/keyrings/yarn.gpg
echo "deb [signed-by=/usr/share/keyrings/yarn.gpg] \
    https://dl.yarnpkg.com/debian/ stable main" \
    >/etc/apt/sources.list.d/yarn.list

apt-get update
apt-get install yarn

yarn --version
```
