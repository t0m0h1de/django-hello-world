FROM docker.io/busybox:latest as downloader

RUN mkdir /tmp/mariadb-data/ \
    && cd /tmp/mariadb-data \
    && wget https://downloads.mysql.com/docs/world-db.tar.gz \
    && tar xzvf ./world-db.tar.gz


FROM docker.io/mariadb:lts-ubi9

COPY --from=downloader /tmp/mariadb-data/world-db/world.sql /docker-entrypoint-initdb.d/
