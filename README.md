```properties
# Install dependencies
yum –y install python3
yum –y install python3-pip
python3 -m venv

# Active ENV
source ./venv/bin/activate
pip install --upgrade pip

# Install Libs
pip3 install scrapy

scrapy startproject voz_crawler
```