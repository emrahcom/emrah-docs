## playwrigh

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

```bash
apt-get install libopengl0 libwoff1 libgles2
```

#### create app

run as `user`

```bash
mkdir -p myplay
cd myplay

npm init playwright
  Do you want to use TypeScript or JavaScript?
    TypeScript
  Where to put your end-to-end tests?
    tests
  Add a GitHub Actions workflow?
    false
  Install Playwright operating system dependencies?
    false
```
