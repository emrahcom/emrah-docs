## jitsi-meet

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

npm install npm -g
```

#### lib-jitsi-meet

don't run as `root`

```bash
cd
git clone https://github.com/jitsi/lib-jitsi-meet.git

cd lib-jitsi-meet
npm install
npm run build
```

#### jitsi-meet

don't run as `root`

```bash
cd
git clone https://github.com/jitsi/jitsi-meet.git

cd jitsi-meet
npm install ../lib-jitsi-meet
npm install
make
```

#### nginx conf

Change all `/usr/share/jitsi-meet` as `/home/your-user-name/jitsi-meet`.

Restart `nginx`

```bash
systemctl restart nginx.service
```
