## minikube & kubectl

Tested on `Debian 11 Bullseye`

#### installation

Install `Docker`. See [Docker notes](docker.md)

Install `kubectl`

```bash
VERSION=$(curl -L -s https://dl.k8s.io/release/stable.txt)
wget -O /tmp/kubectl https://dl.k8s.io/release/$VERSION//bin/linux/amd64/kubectl
install /tmp/kubectl /usr/local/bin/kubectl
```
