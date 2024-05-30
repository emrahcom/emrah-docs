## Testing on MiniKube

```bash
minikube start
minikube addons enable ingress

helm upgrade --install --namespace default --create-namespace \
  --values values.yaml --wait --debug \
  myrelease .

kubectl get ingress
kubectl get pods
kubectl get pv
kubectl get pvc

helm uninstall --namespace default myrelease
```

PV and PVC are keeped even after uninstall. To delete them permanently:

```bash
kubectl get pvc
kubectl delete pvc PVC-Name

kubectl get pvc
kubectl get pv
```
