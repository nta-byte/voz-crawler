#!/bin/bash
docker exec -it voz-crawler-vozdb-1 bash -c 'PGPASSWORD=abcd1234 pg_dump -U postgres -d postgress > /srv/db.sql' 
docker cp voz-crawler-vozdb-1:/srv/db.sql ./crawler/database/ 