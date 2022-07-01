# VOZ crawler
Clone all comments of Stock channel on VOZ

## FE AND BE
location: 
- frontend: app/frontend
- backend: app/backend

```
# run at root project

## up services
docker-compose up -d 

# generate db
./scripts/clone.sh

yarn install
yarn build:shared 

yarn start:fe # run frontend service
yarn start:be # run backend server
```

## CRAWLER MODULE
### Setup ENV

```properties
./scripts/setupEnv.sh # support Centos
./scripts/crawl.sh # run spider to crawling data
```
### Data
- data/comments.csv
- data/comments.xlsx

### Configuration
By default, the script is crawling data from [Stock](https://voz.vn/t/clb-chung-khoan-chia-se-kinh-nghiem-dau-tu-chung-khoan-version-2022.464528) with 30 Codes.

```python
./spiders/voz_stock.py
stockCodes=[
    ...
]
```