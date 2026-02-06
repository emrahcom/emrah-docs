# minikube & kubectl & helm

Tested on `Debian 13 Trixie`.

Set the hostname as `minikube` if this is a VM.

## Installation

### Libvirt or Docker

Install `libvirt` for `kvm2` driver. See [Libvirt notes](libvirt.md)

Install `Docker` for `docker` driver. See [Docker notes](docker-trixie.md)

Looks like `kvm2` is a better option if there are external clients. Use
`iptables` for port-fowarding, not `nftables`...

_**/etc/sysctl.d/90-ip-forward.conf**_

```
net.ipv4.ip_forward=1
```

_**/etc/systemd/system/minikube-iptables.service**_

```
[Unit]
Description=Minikube Iptables Rules
After=network-online.target
After=libvirtd.service
After=libvirt-guest.service

[Service]
Type=oneshot
Environment=MINIKUBE_IP=192.168.39.58
Environment=MINIKUBE_LB1=192.168.39.200
Environment=INTERFACE=enp1s0
ExecStartPre=sleep 3
ExecStartPre=iptables -I FORWARD -p tcp -s ${MINIKUBE_IP} -o ${INTERFACE} -j ACCEPT
ExecStartPre=iptables -I FORWARD -p tcp -i ${INTERFACE} -d ${MINIKUBE_IP} -j ACCEPT
ExecStartPre=iptables -I FORWARD -p udp -s ${MINIKUBE_IP} -o ${INTERFACE} -j ACCEPT
ExecStartPre=iptables -I FORWARD -p udp -i ${INTERFACE} -d ${MINIKUBE_IP} -j ACCEPT
ExecStartPre=iptables -I FORWARD -p tcp -s ${MINIKUBE_LB1} -o ${INTERFACE} -j ACCEPT
ExecStartPre=iptables -I FORWARD -p tcp -i ${INTERFACE} -d ${MINIKUBE_LB1} -j ACCEPT
ExecStartPre=iptables -I FORWARD -p udp -s ${MINIKUBE_LB1} -o ${INTERFACE} -j ACCEPT
ExecStartPre=iptables -I FORWARD -p udp -i ${INTERFACE} -d ${MINIKUBE_LB1} -j ACCEPT
ExecStartPre=iptables -t nat -I PREROUTING -i ${INTERFACE} -p tcp --dport 443 -j DNAT --to ${MINIKUBE_IP}
ExecStartPre=iptables -t nat -I PREROUTING -i ${INTERFACE} -p tcp --dport 3478 -j DNAT --to ${MINIKUBE_LB1}
ExecStartPre=iptables -t nat -I PREROUTING -i ${INTERFACE} -p udp --dport 3478 -j DNAT --to ${MINIKUBE_LB1}
ExecStartPre=iptables -t nat -I PREROUTING -i ${INTERFACE} -p tcp --dport 30000:30099 -j DNAT --to ${MINIKUBE_IP}
ExecStartPre=iptables -t nat -I PREROUTING -i ${INTERFACE} -p tcp --dport 30101:32767 -j DNAT --to ${MINIKUBE_IP}
ExecStartPre=iptables -t nat -I PREROUTING -i ${INTERFACE} -p udp --dport 30000:32767 -j DNAT --to ${MINIKUBE_IP}
ExecStartPre=iptables -t nat -I POSTROUTING -s ${MINIKUBE_IP} -o ${INTERFACE} -j MASQUERADE
ExecStart=true
RemainAfterExit=yes
ExecStop=true
ExecStopPost=iptables -t nat -D POSTROUTING -s ${MINIKUBE_IP} -o ${INTERFACE} -j MASQUERADE
ExecStopPost=iptables -t nat -D PREROUTING -i ${INTERFACE} -p udp --dport 30000:32767 -j DNAT --to ${MINIKUBE_IP}
ExecStopPost=iptables -t nat -D PREROUTING -i ${INTERFACE} -p tcp --dport 30101:32767 -j DNAT --to ${MINIKUBE_IP}
ExecStopPost=iptables -t nat -D PREROUTING -i ${INTERFACE} -p tcp --dport 30000:30099 -j DNAT --to ${MINIKUBE_IP}
ExecStopPost=iptables -t nat -D PREROUTING -i ${INTERFACE} -p udp --dport 3478 -j DNAT --to ${MINIKUBE_LB1}
ExecStopPost=iptables -t nat -D PREROUTING -i ${INTERFACE} -p tcp --dport 3478 -j DNAT --to ${MINIKUBE_LB1}
ExecStopPost=iptables -t nat -D PREROUTING -i ${INTERFACE} -p tcp --dport 443 -j DNAT --to ${MINIKUBE_IP}
ExecStopPost=iptables -D FORWARD -p udp -i ${INTERFACE} -d ${MINIKUBE_LB1} -j ACCEPT
ExecStopPost=iptables -D FORWARD -p udp -s ${MINIKUBE_LB1} -o ${INTERFACE} -j ACCEPT
ExecStopPost=iptables -D FORWARD -p tcp -i ${INTERFACE} -d ${MINIKUBE_LB1} -j ACCEPT
ExecStopPost=iptables -D FORWARD -p tcp -s ${MINIKUBE_LB1} -o ${INTERFACE} -j ACCEPT
ExecStopPost=iptables -D FORWARD -p udp -i ${INTERFACE} -d ${MINIKUBE_IP} -j ACCEPT
ExecStopPost=iptables -D FORWARD -p udp -s ${MINIKUBE_IP} -o ${INTERFACE} -j ACCEPT
ExecStopPost=iptables -D FORWARD -p tcp -i ${INTERFACE} -d ${MINIKUBE_IP} -j ACCEPT
ExecStopPost=iptables -D FORWARD -p tcp -s ${MINIKUBE_IP} -o ${INTERFACE} -j ACCEPT

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

```bash
systemctl daemon-reload
systemctl enable minikube-iptables.service
systemctl start minikube-iptables.service
```

### packages

```bash
apt-get install curl gnupg
```

### kubectl

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

Create the source file. Update the version according to the latest release.

_**/etc/apt/sources.list.d/kubernetes.sources**_

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

Run it as `user`:

```bash
kubectl version
```

### krew

This is the package management plugin for `kubectl`. Don't install it if not
really needed. Install it as `user`:

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

### minikube

Install `minikube` as `root`:

```bash
wget -O /tmp/minikube \
    https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
install /tmp/minikube /usr/local/bin/minikube
```

And start it as `user`:

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

Enable `metallb`:

```bash
# Use the same range for metallb IPs
minikube ip
minikube addons enable metallb
minikube addons configure metallb
  start: 192.168.39.200
  end: 192.168.39.220
```

Install `cert-manager`:

```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.19.3/cert-manager.yaml
kubectl -n cert-manager get pods
```

Create `local-issuer.yaml` to add a self-signed issuer :

```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: selfsigned-issuer
spec:
  selfSigned: {}
```

And add it:

```bash
kubectl apply -f local-issuer.yaml
kubectl get clusterissuer
```

To delete all local clusters:

```bash
minikube delete --all
```

### helm

Install `helm` as `root`:

```bash
wget -O /tmp/get_helm.sh \
    https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
bash /tmp/get_helm.sh
```

And run it as `user`:

```bash
helm version
```

## ArgoCD

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

## command examples

Lint:

```bash
helm lint --set key=value -f values.my.yaml .
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

Repo:

```bash
helm repo --help
helm repo list
helm repo add jitsi https://jitsi-contrib.github.io/jitsi-helm/
helm repo remove jitsi
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

## links

- https://artifacthub.io/
