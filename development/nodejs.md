# nodejs

Tested on `Debian 13 Trixie`

### packages

run as `root`

```bash
wget -qO /tmp/nodesource.gpg.key \
    https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key
cat /tmp/nodesource.gpg.key | gpg --dearmor \
    >/usr/share/keyrings/nodesource.gpg

#echo "deb [signed-by=/usr/share/keyrings/nodesource.gpg] \
#    https://deb.nodesource.com/node_24.x nodistro main" \
#    >/etc/apt/sources.list.d/nodesource.list

cat <<EOF >/etc/apt/sources.list.d/nodesource.sources
Types: deb
URIs: https://deb.nodesource.com/node_24.x/
Suites: nodistro
Components: main
Signed-By: /usr/share/keyrings/nodesource.gpg
EOF

apt-get update
apt-get install nodejs
```

### npm upgrade

```bash
npm install -g npm
```

### purge

If `nodejs` is already installed from the Debian repo, purge it as below before
installing it from the `nodejs` repo.

```bash
apt-get purge nodejs

rm -rf /usr/lib/node_modules
rm -rf /usr/local/lib/node_modules
```
