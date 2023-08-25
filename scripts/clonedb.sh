#!/bin/bash
docker cp ./crawler/databases/create-db.sql voz-crawler-vozdb-1:/srv/create-db.sql
docker exec -it voz-crawler-vozdb-1 bash -c 'PGPASSWORD=${POSTGRES_PASSWORD} psql -U ${POSTGRES_USER} -c "drop database ${POSTGRES_DB};"'
docker exec -it voz-crawler-vozdb-1 bash -c 'PGPASSWORD=${POSTGRES_PASSWORD} psql -U ${POSTGRES_USER} -c "create database ${POSTGRES_DB};"'
docker exec -it voz-crawler-vozdb-1 bash -c 'PGPASSWORD=${POSTGRES_PASSWORD} psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} -f /srv/create-db.sql'
