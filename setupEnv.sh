#!/bin/bash
# yum –y install python3
# yum –y install python3-pip
python3 -m venv venv
source ./venv/bin/activate
pip install --upgrade pip

pip install scrapy
pip install openpyxl
pip install psycopg2
pip install psycopg2-binary==2.8.6