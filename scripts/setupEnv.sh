#!/bin/bash
apt install python3 -y
apt install python3-pip -y
python3 -m venv venv
source ./venv/bin/activate
pip install --upgrade pip

pip install scrapy
pip install pandas
pip install sqlalchemy
pip install openpyxl
pip install psycopg2
pip install psycopg2-binary==2.8.6