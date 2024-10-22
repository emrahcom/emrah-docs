## docker & docker-compose

Tested on `Debian Bookworm`.

#### installation

```bash
wget -qO /tmp/docker.gpg.key https://download.docker.com/linux/debian/gpg
cat /tmp/docker.gpg.key | gpg --dearmor >/usr/share/keyrings/docker.gpg
echo "deb [signed-by=/usr/share/keyrings/docker.gpg] \
  https://download.docker.com/linux/debian bookworm stable" \
  >/etc/apt/sources.list.d/docker.list

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
