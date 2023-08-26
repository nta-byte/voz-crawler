#!/usr/bin/env bash

echo "crawling data ..."
scrapy crawl voz_stock
python -m crawler.scripts.generate_stats_report
