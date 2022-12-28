## nodejs

Tested on `Debian 11 Bullseye`

#### packages

run as `root`

```bash
wget -qO /tmp/nodesource.gpg.key \
    https://deb.nodesource.com/gpgkey/nodesource.gpg.key
cat /tmp/nodesource.gpg.key | gpg --dearmor \
    >/usr/share/keyrings/nodesource.gpg
echo "deb [signed-by=/usr/share/keyrings/nodesource.gpg] \
    https://deb.nodesource.com/node_16.x bullseye main" \
    >/etc/apt/sources.list.d/nodesource.list

apt-get update
apt-get install nodejs
```
