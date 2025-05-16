# Custom Jitsi Helm Chart

Tested on `Debian 13 Trixie` with `minikube`.

### Cluster

Start `minikube`:

```bash
minukube start
```

### Chart.yaml

```yaml
apiVersion: v2
name: my-jitsi
description: A Helm chart for Jitsi
version: 0.1.0
dependencies:
  - name: jitsi-meet
    version: 1.4.1
    repository: https://jitsi-contrib.github.io/jitsi-helm
    alias: jitsi
```

### Dependencies

```bash
helm dependency update
```

### myvalues.yaml

Create `myvalues.yaml` by only using critical values from the default
`values.yaml` of `jitsi-meet` chart. The values should be under `jitsi:` tag.

To show the default `values.yaml`:

```bash
helm show values charts/jitsi-meet-1.4.1.tgz
```

A few lines from our `myvalues.yaml`:

```yaml
jitsi:
  publicURL: "meet.minikube.loc"

  web:
    replicaCount: 1
    image:
      repository: jitsi/web
      tag: "stable-10184"
```


### Install

```bash
helm install myjitsi . -f myvalues.yaml

kubectl get pods
kubectl get ingress
```

### Uninstall

```bash
helm uninstall myjitsi
```

### Links

- https://github.com/jitsi-contrib/jitsi-helm
