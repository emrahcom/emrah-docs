## minikube & kubectl

Tested on `Debian 11 Bullseye`

#### installation

Install `Docker`. See [Docker notes](docker.md)

Install `kubectl` as `root`

```bash
VERSION=$(curl -L -s https://dl.k8s.io/release/stable.txt)
wget -O /tmp/kubectl https://dl.k8s.io/release/$VERSION//bin/linux/amd64/kubectl
install /tmp/kubectl /usr/local/bin/kubectl
```

Install `minikube` as `root`

```bash
wget -O /tmp/minikube \
    https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
install /tmp/minikube /usr/local/bin/minikube
```

#### start

```bash
minikube start

kubectl get pods -A
```
