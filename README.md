# Django Hello World

## Deploy app to OpenShift using new-app command

```
oc new-app python:3.12-ubi9~https://github.com/t0m0h1de/django-hello-world --name <app-name> -e DB_DATABASENAME=<mariadb database name> -e DB_USER=<mariadb user name> -e DB_PASSWORD=<mariadb user password> -e DB_HOST=<mariadb service host name> -e DB_PORT=3306
```

## Deploy MariaDB to OpenShift using helm

```
helm install <package name> ./helm-package/mariadb-polls
```

Note: `<package name>` must be the same name of `<mariadb service host name>`
