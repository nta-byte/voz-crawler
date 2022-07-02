#!/bin/bash
docker exec -it voz-crawler-vozdb-1 bash -c 'PGPASSWORD=abcd1234 pg_dump -U postgres -d postgress > /srv/db-latest.sql' 
docker cp voz-crawler-vozdb-1:/srv/db-latest.sql ./crawler/databases/
cp -r ./crawler/databases/db-latest.sql ./crawler/databases/db-$(date +'%y%m%d_%H%M')
