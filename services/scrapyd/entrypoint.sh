#!/usr/bin/env bash

wait-for-it $PG_HOST:$PG_PORT -t 60
wait-for-it $NGINX_HOST:$NGINX_PORT -t 60
chmod +x scripts/crawlnew.sh
chmod +x scripts/clonedb.sh
./scripts/clonedb.sh
./scripts/crawlnew.sh