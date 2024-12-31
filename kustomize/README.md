# Kustomiza manifest

## Kustomize MariaDB manifest

1. Compile overall yaml manifest file from helm package

```
helm template <package name> ../helm-package/mariadb-polls > ./base/app.yaml
```

2. Kustomize manifest and overlay

* production

```
oc kustomize kustomize/overlays/production
```

* staging

```
oc kustomize kustomize/overlays/staging
```
