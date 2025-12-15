# yarn

Tested on `Debian 13 Trixie`

### packages

run as `root`

```bash
wget -qO /tmp/yarn.gpg.key https://dl.yarnpkg.com/debian/pubkey.gpg
cat /tmp/yarn.gpg.key | gpg --dearmor >/usr/share/keyrings/yarn.gpg

#echo "deb [signed-by=/usr/share/keyrings/yarn.gpg] \
#    https://dl.yarnpkg.com/debian/ stable main" \
#    >/etc/apt/sources.list.d/yarn.list

cat <<EOF >/etc/apt/sources.list.d/yarn.sources
Types: deb
URIs: https://dl.yarnpkg.com/debian/
Suites: stable
Components: main
Signed-By: /usr/share/keyrings/yarn.gpg
EOF

apt-get update
apt-get install yarn

yarn --version
```

### Commands

##### install

Install packages

```bash
yarn install
```

##### outdated

Show outdated packages:

```bash
yarn outdated
```
