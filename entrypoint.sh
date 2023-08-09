#!/usr/bin/env bash

wait-for-it $PG_HOST:5432 -t 60
wait-for-it $NGINX_HOST:6379 -t 60
chmod +x scripts/crawl.sh
./scripts/crawl.sh