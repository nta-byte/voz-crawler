#!/bin/bash
source ./venv/bin/activate
echo "crawling data ..."
scrapy crawl voz_stock
python -m crawler.scripts.generate_stats_report

if [ -d "/mnt/e/" ]; then
    cp -r ./crawler/data/voz_data-latest.* "/mnt/e/"
fi