## ory-kratos

Tested on _Debian 11 Bullseye_ LXC container. See [Docker notes](docker.md).

#### base packages

```bash
apt-get install git
```

#### kratos clone

```bash
cd
git clone https://github.com/ory/kratos.git
```

#### checkout to tag

```bash
cd kratos
git tag | tail
git checkout v0.7.1-alpha.1
```

#### kratos run

```bash
docker-compose -f quickstart.yml -f quickstart-standalone.yml up --build \
    --force-recreate
```

#### kratos clean up

```bash
docker-compose -f quickstart.yml down -v
docker-compose -f quickstart.yml rm -fsv
docker ps
```

#### links

- [Ory Kratos Quickstart](https://www.ory.sh/kratos/docs/quickstart/)
