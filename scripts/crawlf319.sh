#!/usr/bin/env bash

echo "crawling data ..."
scrapy crawl f319
python -m crawler.scripts.generate_stats_report
