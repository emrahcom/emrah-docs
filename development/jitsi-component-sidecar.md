## jitsi-component-sidecar

Tested on `Debian 11 Bullseye`

### packages

Install `nodejs` (_16.x or newer_). See [nodejs](./nodejs.md).

### repo

```bash
git clone https://github.com/jitsi/jitsi-component-sidecar.git

cd jitsi-component-sidecar
npm install
```

### development

Edit codes.

### bundle

```bash
npm run build
```

The bundle will be created as `bundle/app.js`. Replace it with
`/usr/share/jitsi-component-sidecar/app.js` in `component-sidecar` server.
