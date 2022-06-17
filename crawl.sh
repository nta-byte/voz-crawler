#!/bin/bash
echo "crawling data ..."
scrapy crawl voz_stock


if [ -d "/mnt/e/" ]; then
    cp -r ./data/comments.* "/mnt/e/"
fi