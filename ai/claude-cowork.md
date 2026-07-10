## Claude Cowork

#### Installation

Run as `root`:

```bash
curl -fsSLo /usr/share/keyrings/claude-desktop-archive-keyring.asc \
  https://downloads.claude.ai/claude-desktop/key.asc

cat > /etc/apt/sources.list.d/claude-desktop.sources <<EOF
Types: deb
URIs: https://downloads.claude.ai/claude-desktop/apt/stable
Suites: stable
Components: main
Signed-By: /usr/share/keyrings/claude-desktop-archive-keyring.asc
EOF

apt-get update
apt-get install claude-desktop virtiofsd --no-install-recommends

adduser emrah kvm
ln -s /usr/lib/qemu/virtiofsd /usr/bin/virtiofsd
```

## Running

Use as the normal user:

```bash
claude-desktop
```
