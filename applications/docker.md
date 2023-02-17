## docker & docker-compose

Tested on `Debian Bullseye`.

#### installation

```bash
apt-get install docker-compose --install-recommends
```

#### permission

Add the user account to `docker` group.

```bash
adduser emrah docker
```

#### version

```bash
docker --version
docker-compose --version
```

#### test

```bash
docker run hello-world
```

#### docker in LXC

```config
lxc.include = /usr/share/lxc/config/nesting.conf
lxc.apparmor.profile = unconfined
lxc.apparmor.allow_nesting = 1

lxc.cgroup2.devices.allow = c 10:200 rwm
```

_It doesn't work in an ephemeral container._

#### commands

```bash
docker ps
docker exec -it <CONTAINER-ID> /bin/sh
```

- -i interactive
- -t tty
