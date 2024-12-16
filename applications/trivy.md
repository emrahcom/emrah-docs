# Trivy

## Installation

Tested on Debian 12 Bookworm. As `root`:

```bash
wget -qO /tmp/trivy.key https://aquasecurity.github.io/trivy-repo/deb/public.key
cat /tmp/trivy.key | gpg --dearmor >/usr/share/keyrings/trivy.gpg
echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] \
  https://aquasecurity.github.io/trivy-repo/deb generic main" \
  >/etc/apt/sources.list.d/trivy.list

apt-get update
apt-get install trivy
```

## Usage

```bash
trivy --version

trivy image ghcr.io/nordeck/jitsi-keycloak-adapter
trivy image ghcr.io/nordeck/jitsi-keycloak-adapter \
  --scanners vuln --severity CRITICAL
```

## Links

- https://trivy.dev/latest/getting-started/installation
