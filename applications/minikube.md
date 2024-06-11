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

Run it as `user`

```bash
kubectl version
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
kubectl exec --stdin --tty <POD-NAME> -- /bin/bash
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
