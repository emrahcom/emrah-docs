# Jibri

Tested on `Debian 11 Bullseye`

### packages

```bash
apt-get install git
apt-get install maven openjdk-11-jdk-headless
```

### repo

```bash
git clone https://github.com/jitsi/jibri.git
```

### build

```bash
cd jibri
mvn -B clean verify package -DskipTests
```

### deployment

Copy `target/jibri-8.0-SNAPSHOT-jar-with-dependencies.jar` as
`/opt/jitsi/jibri/jibri.jar` to `Jibri` server.
