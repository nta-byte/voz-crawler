#!/bin/bash
docker cp ./crawler/databases/create-db.sql voz-crawler-vozdb-1:/srv/create-db.sql
docker exec -it voz-crawler-vozdb-1 bash -c 'PGPASSWORD=abcd1234 psql -U postgres -c "drop database postgress;"' 
docker exec -it voz-crawler-vozdb-1 bash -c 'PGPASSWORD=abcd1234 psql -U postgres -c "create database postgress;"' 
docker exec -it voz-crawler-vozdb-1 bash -c 'PGPASSWORD=abcd1234 psql -U postgres -d postgress -f /srv/create-db.sql'
