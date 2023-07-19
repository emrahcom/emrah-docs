## rancher

### Accessing the remote cluster

- open the cluster
- download `kubeconfig`
- copy `kubeconfig` as `~/.kube/config.mycode.rancher`

### Namespace

- open the cluster
- create a project
- create a namespace inside this project

### Test

```bash
kubectl --kubeconfig ~/.kube/config.mycode.rancher -n my-namespace get pods
helm --kubeconfig ~/.kube/config.mycode.rancher -n my-namespace ls
```
