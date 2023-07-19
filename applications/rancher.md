## rancher

### Accessing the remote cluster

- open the cluster
- download `kubeconfig`
- backup the default config as `~/.kube/config.old`
- copy `kubeconfig` as `~/.kube.config`

### Namespace

- open the cluster
- create a project
- create a namespace inside this project

### kubectl

```bash
kubectl -n my-name-space get pods
```
