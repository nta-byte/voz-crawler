# VOZ crawler
cloning all comments of the Stock channel on VOZ

## Packages (includes frontend and backend)
location: 
- frontend: app/frontend
- backend: app/backend

```
# run at root project

## up the related services
docker-compose up -d 

# generate db (do this at the first time)
./scripts/clone.sh

# install dependencies
yarn install

# build common libs
yarn build:shared 

# start frontend service
yarn start:fe

# start backend service
yarn start:be # run backend server
```

## Crawler service
### Setup

```properties
# prepare env for crawl job (just support centos env)
./scripts/setupEnv.sh

# crawling data
./scripts/crawl.sh
```

### Data
- data/comments.csv
- data/comments.xlsx

### Database
- location: **./crawler/databases/\***
- update the database backup: **./script/dump.sh**

### Configuration
By default, the script is crawling data from [Stock](https://voz.vn/t/clb-chung-khoan-chia-se-kinh-nghiem-dau-tu-chung-khoan-version-2022.464528) with 30 Codes.

```python
./spiders/voz_stock.py
stockCodes=[
    ...
]
```
