# VOZ crawler
Clone all comments of Stock channel on VOZ

## Setup ENV

```properties
./setupEnv.sh # support Centos
./crawl.sh # run spider to crawling data
```
## Data
- data/comments.csv
- data/comments.xlsx

## Configuration
By default, the script is crawling data from [Stock](https://voz.vn/t/clb-chung-khoan-chia-se-kinh-nghiem-dau-tu-chung-khoan-version-2022.464528) with 30 Codes.

```python
./spiders/voz_stock.py
stockCodes=[
    ...
]
```