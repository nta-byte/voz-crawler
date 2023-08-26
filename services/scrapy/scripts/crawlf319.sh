#!/usr/bin/env bash

echo "crawling data ..."
scrapy crawl f319_stock
python -m crawler.scripts.generate_stats_report
