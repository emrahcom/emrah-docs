# Jitsi Helm Chart

Tested on `Debian 13 Trixie` with `minikube`.

### Cluster

Start `minikube`:

```bash
minukube start
```

### Helm Chart Repository

Add `jitsi-helm` repo:

```bash
helm repo list
helm repo add jitsi https://jitsi-contrib.github.io/jitsi-helm
```

### Deployment

```bash
mkdir jitsi-helm
cd jitsi-helm
```

Get the default values:

```bash
helm show values jitsi/jitsi-meet > myvalues.yaml
```

Customize `myvalues.yaml` according to requirements:

Deploy:

```bash
helm install myjitsi jitsi/jitsi-meet -f myvalues.yaml
```

### Uninstall

```bash
helm uninstall myjitsi
```

### Links

- https://github.com/jitsi-contrib/jitsi-helm
