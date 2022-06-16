#!/bin/bash
fileName=comments-all-$(date +'%Y-%m-%d%H%M')
# fileName=comments-all-2022-06-161135
fromPath=data/$fileName.json
targetPath=data/comments-all-latest.json

echo "crawling data ..."
# scrapy crawl voz_stock -o $fromPath

echo "sync raw data"
cp -r $fromPath $targetPath

echo "processing data"
python scripts/push_all_data_db.py

if [ -d "/mnt/e/" ]; then
    cp -r ./data/comments.* "/mnt/e/"
fi