## minikube & kubectl & helm

Tested on `Debian 11 Bullseye`

#### Installation

##### Docker

Install `Docker`. See [Docker notes](docker.md)

##### kubectl

Install `kubectl` as `root`

```bash
VERSION=$(curl -L -s https://dl.k8s.io/release/stable.txt)
wget -O /tmp/kubectl https://dl.k8s.io/release/$VERSION//bin/linux/amd64/kubectl
install /tmp/kubectl /usr/local/bin/kubectl
```

##### minikube

Install `minikube` as `root`

```bash
wget -O /tmp/minikube \
    https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
install /tmp/minikube /usr/local/bin/minikube
```

And start it as `user`

```bash
minikube start

kubectl get nodes
kubectl get pods -A
```

To delete all local clusters

```bash
minikube delete --all
```

##### helm

Install `helm` as `root`

```bash
wget -O /tmp/get_helm.sh \
    https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
bash /tmp/get_helm.sh
```

And run it as `user`

```bash
helm version
```
