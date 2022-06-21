#!/bin/bash
source ./venv/bin/activate
echo "crawling data ..."
scrapy crawl voz_stock


if [ -d "/mnt/e/" ]; then
    cp -r ./data/voz_data-latest.* "/mnt/e/"
fi