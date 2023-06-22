## Jitsi

### Docker-Compose

#### Download

Download
[the lastest stable](https://github.com/jitsi/docker-jitsi-meet/releases):

```bash
ARCHIVE="https://github.com/jitsi/docker-jitsi-meet/archive/refs/tags"
wget $ARCHIVE/stable-8719.tar.gz
```

#### Extract

```bash
tar xzf stable-8719.tar.gz
```

#### Environment file

Create `.env`:

```bash
cd docker-jitsi-meet-stable-8719
cp env.example .env
```

#### Secrets

Generate secrets:

```bash
./gen-passwords.sh
```

#### Local directories

Create local directories:

```bash
mkdir -p ~/.jitsi-meet-cfg/{web,transcripts,prosody/config}
mkdir -p ~/.jitsi-meet-cfg/{prosody/prosody-plugins-custom,jicofo,jvb}
mkdir -p ~/.jitsi-meet-cfg/{jigasi,jibri}
```

#### First run

```bash
docker-compose up -d
docker-compose ps
docker-compose down
```

#### Customization

Update environment variables in `.env`.

- `PUBLIC_URL`

  _e.g. https://jitsi.docker.corp_

Check `.jitsi-meet-cfg` folder for created config files and further
customizations.

#### Reverse proxy

Put `Jitsi` behind a reverse proxy such as `Nginx`

```conf
server_names_hash_bucket_size 64;

server {
  listen 443 ssl;
  listen [::]:443 ssl;

  include snippets/snakeoil.conf;
  server_name jitsi.docker.corp;

  location = /xmpp-websocket {
    proxy_pass http://172.18.18.1:8000;
    proxy_http_version 1.1;
    proxy_set_header Host $http_host;
    proxy_set_header X-Forwarded-For $remote_addr;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    tcp_nodelay on;
  }

  location ~ ^/colibri-ws/default-id/(.*) {
    proxy_pass http://172.18.18.1:8000;
    proxy_http_version 1.1;
    proxy_set_header Host $http_host;
    proxy_set_header X-Forwarded-For $remote_addr;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    tcp_nodelay on;
  }

  location / {
    proxy_pass http://172.18.18.1:8000;
    proxy_http_version 1.1;
    proxy_set_header Host $http_host;
    proxy_set_header X-Forwarded-For $remote_addr;
    proxy_set_header Connection "";
  }
}
```

#### DNS records

`Jitsi` domain should point to the IP address of the reverse proxy.\
_e.g. jitsi.docker.corp -> 172.18.18.40_

#### References

See
[Jitsi Docker Guide](https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-docker/)

### Additional notes

#### Multiple local pairs for `jvb`

```bash
# don't disable STUN in sip-communicator.properties
hocon -f /etc/jitsi/videobridge/jvb.conf set \
  ice4j.harvest.mapping.stun.enabled true

# first local pair
hocon -f /etc/jitsi/videobridge/jvb.conf set \
  ice4j.harvest.mapping.static-mappings.0.local-address 172.22.22.14
hocon -f /etc/jitsi/videobridge/jvb.conf set \
  ice4j.harvest.mapping.static-mappings.0.public-address 192.168.1.56

# second local pair
hocon -f /etc/jitsi/videobridge/jvb.conf set \
  ice4j.harvest.mapping.static-mappings.1.local-address 172.22.22.14
hocon -f /etc/jitsi/videobridge/jvb.conf set \
  ice4j.harvest.mapping.static-mappings.1.public-address 10.1.1.56

systemctl restart jitsi-videobridge2.service
```
