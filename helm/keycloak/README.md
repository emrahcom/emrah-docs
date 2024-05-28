## Testing on MiniKube

```bash
minikube start
minikube addons enable ingress

helm upgrade --install --namespace default --create-namespace \
  --values values.yaml --wait --debug \
  myrelease .

kubectl get pods
kubectl get ingress

helm uninstall --namespace default myrelease
```
