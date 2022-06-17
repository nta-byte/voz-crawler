# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from VOZ_crawler.utils import pypg


class VozCrawlerPipeline:
    def process_item(self, item, spider):
        client = pypg.PYPG()
        data = ItemAdapter(item).asdict()
        client.voz_rawcomment_insert(data)
        return item
