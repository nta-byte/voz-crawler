#!/bin/bash
docker exec -it crawler-vozdb-1 bash -c 'PGPASSWORD=abcd1234 pg_dump -U postgres >> /srv/db.sql' 
docker cp crawler-vozdb-1:/srv/db.sql ./crawler/database/ 