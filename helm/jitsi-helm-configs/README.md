# Commands

```bash
helm show values .

#helm install myjitsi . -f jitsi-helm-configs/myvalues.v1.yaml

helm install myjitsi . -f jitsi-helm-configs/myvalues.hostport-range.yaml
helm install myjitsi . -f jitsi-helm-configs/myvalues.hostport-coturn.yaml

kubectl get pods

helm upgrade myjitsi .

helm uninstall myjitsi
```
