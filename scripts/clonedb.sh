#!/bin/bash
docker cp ./crawler/database/db-latest.sql voz-crawler-vozdb-1:/srv/db-latest.sql
docker exec -it voz-crawler-vozdb-1 bash -c 'PGPASSWORD=abcd1234 psql -U postgres -c "drop database postgress;"' 
docker exec -it voz-crawler-vozdb-1 bash -c 'PGPASSWORD=abcd1234 psql -U postgres -c "create database postgress;"' 
docker exec -it voz-crawler-vozdb-1 bash -c 'PGPASSWORD=abcd1234 psql -U postgres -d postgress -f /srv/db-latest.sql' 
