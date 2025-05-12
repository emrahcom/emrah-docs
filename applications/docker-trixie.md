## docker & docker-compose

Tested on `Debian Trixie`.

#### packages

```bash
apt-get update
apt-get install gpg
```

#### installation

```bash
wget -qO /tmp/docker.gpg.key https://download.docker.com/linux/debian/gpg
cat /tmp/docker.gpg.key | gpg --dearmor >/usr/share/keyrings/docker.gpg

cat <<EOF >/etc/apt/sources.list.d/docker.sources
Types: deb
URIs: https://download.docker.com/linux/debian/
Suites: trixie
Components: stable
Signed-By: /usr/share/keyrings/docker.gpg
EOF

apt-get update
apt-get install docker-ce docker-buildx-plugin docker-compose-plugin

docker --version
docker compose version
```

#### permission

Add the user account to `docker` group.

```bash
adduser emrah docker
```
