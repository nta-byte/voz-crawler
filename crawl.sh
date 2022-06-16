#!/bin/bash
fileName=comments-$(date +'%Y-%m-%d%H%M')
fromPath=data/$fileName.json
targetPath=data/comments-latest.json

echo "crawling data ..."
scrapy crawl voz_stock -o $fromPath

echo "backuping ..."
rm -rf $targetPath
cp -r $fromPath $targetPath

python ./scripts/convert_json_csv.py
echo "DONE"