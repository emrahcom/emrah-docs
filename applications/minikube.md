## minikube & kubectl & helm

Tested on `Debian 13 Trixie`

#### Installation

##### Docker

Install `Docker`. See [Docker notes](docker-trixie.md)

##### kubectl

Install `kubectl` as `root`.

Learn the available version:

```bash
VERSION=$(curl -L -s https://dl.k8s.io/release/stable.txt  | cut -d '.' -f1-2)
echo $VERSION
```

Download Kubernetes GPG key:

```bash
wget -qO /tmp/kubernetes.gpg.key https://pkgs.k8s.io/core:/stable:/$VERSION/deb/Release.key
cat /tmp/kubernetes.gpg.key | gpg --dearmor >/usr/share/keyrings/kubernetes.gpg
```

Create _/etc/apt/sources.list.d/kubernetes.sources_. Update the version
according the latest release:

```
Types: deb
URIs: https://pkgs.k8s.io/core:/stable:/v1.33/deb/
Suites: /
Components:
Signed-By: /usr/share/keyrings/kubernetes.gpg
```

Install the package:

```bash
apt-get update
apt-get install kubectl
```

Run it as `user`

```bash
kubectl version
```

##### krew

This is the package management plugin for `kubectl`. Install it as `user`:

```bash
cd /tmp
wget -O krew-linux_amd64.tar.gz \
  https://github.com/kubernetes-sigs/krew/releases/latest/download/krew-linux_amd64.tar.gz
tar zxf krew-linux_amd64.tar.gz
./krew-linux_amd64 install krew
```

Add `krew` into `PATH`. In `~/.zshrc`:

```
export PATH=$PATH:~/bin:~/.krew/bin
```

Test it:

```bash
kubectl krew
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
kubectl get all
```

Enable `ingress`:

```bash
minikube addons list
minikube addons enable ingress
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

#### ArgoCD

Install it using the normal user account:

```bash
kubectl create namespace argocd
kubectl apply -n argocd \
  -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

kubectl get namespaces
kubectl -n argocd get pods
```

ArgoCD UI:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o json | \
  jq -r .data.password | base64 --decode
kubectl -n argocd get svc
kubectl -n argocd port-forward svc/argocd-server 8443:443
```

Go to [https://127.0.0.1:8443](https://127.0.0.1:8443). Use `admin` as username.

#### command examples

Lint:

```bash
helm lint .
```

Check templates:

```bash
helm template --set key=value -f values.my.yaml myrelease .
```

Deployment:

```bash
helm upgrade --install --namespace default \
  --set key1=value1 --set key2=value2 \
  -f values.my.yaml \
  <RELEASE-NAME> <CHART-PATH>

kubectl get all
```

Uninstall:

```bash
helm uninstall --namespace default <RELEASE-NAME>
```

To attach to a container in `Minicube`:

```bash
kubectl get pods
kubectl exec -it <POD-NAME> -- /bin/bash
```

To attach to a container in a specific container:

```bash
kubectl --kubeconfig ~/.kube/config.mycluster -n mynamespace get pods
kubectl --kubeconfig ~/.kube/config.mycluster -n mynamespace exec it <POD-NAME> -- /bin/bash
```

Port forwarding:

```bash
kubectl get services
kubectl port-forward --address 0.0.0.0 service/<NAME> 8080:80
```

Logs:

```bash
minikube logs
kubectl logs <POD-NAME>
kubectl logs -f <POD-NAME>
```

Ingress logs:

```bash
kubectl logs -n ingress-nginx -l app.kubernetes.io/name=ingress-nginx
```

File copy:

```bash
kubectl cp somefile <POD-NAME>:/tmp/
kubectl cp <POD-NAME>:/tmp/somefile /tmp/
```

Minikube addons:

```bash
kubectl get pods -A

minikube addons list
minikube addons enable ingress

kubectl get pods -A
kubectl get ingress
```

Minikube storage:

```bash
kubectl get storageclass
kubectl get pvc
kubectl get pv

kubectl delete pvc pvc-name
kubectl delete pv pv-name
```

Image pull secret:

First, create a personal access token (classic) in GitHub to be able to pull
private packages.

```bash
export GITHUB_TOKEN=...
echo $GITHUB_TOKEN | \
  docker login ghcr.io -u YOUR_GITHUB_USERNAME --password-stdin
```

This token will go to `~/.docker/config.json`. Then create the secret for
`Minikube`:

```bash
kubectl create secret generic regcred \
  --from-file=.dockerconfigjson=/home/emrah/.docker/config.json \
  --type=kubernetes.io/dockerconfigjson
kubectl get secret
```

#### links

- https://artifacthub.io/
