# base image
FROM mdillon/postgis

RUN apt-get update \
    && apt-get install -y curl zip \
    && apt-get clean

COPY ./my_intersections.dump /docker-entrypoint-initdb.d/my_intersections.dump
COPY ./mkintersectiondb.sh /docker-entrypoint-initdb.d/qmkintersectiondb.sh
COPY ./sql /docker-entrypoint-initdb.d/sql/

RUN chmod +x /docker-entrypoint-initdb.d/qmkintersectiondb.sh