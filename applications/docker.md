## docker & docker-compose

Tested on `Debian Bullseye`.

#### installation

```bash
apt-get install docker-compose --install-recommends
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
