## jitsi-meet

Tested on `Debian 11 Bullseye`

#### packages

Install `nodejs` (_16.x or newer_). See [nodejs](./nodejs.md).

#### lib-jitsi-meet

don't run as `root`

```bash
cd
git clone https://github.com/jitsi/lib-jitsi-meet.git

cd lib-jitsi-meet
npm install
npm run build
```

#### jitsi-meet

don't run as `root`, reserve at least 16 GB RAM.

```bash
cd
git clone https://github.com/jitsi/jitsi-meet.git

cd jitsi-meet
npm install ../lib-jitsi-meet
npm install
make
```

#### nginx conf

Change all `/usr/share/jitsi-meet` as `/home/your-user-name/jitsi-meet` in your
`Nginx` site config file.

Restart `nginx`

```bash
systemctl restart nginx.service
```
