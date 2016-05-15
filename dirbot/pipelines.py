from scrapy.exceptions import DropItem
import pymongo
from scrapy.conf import settings
from scrapy import log



class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    words_to_filter = ['Female', 'Male']

    def process_item(self, item):
        for word in self.words_to_filter:
            if word in unicode(item['description']).lower():
                raise DropItem("!!!!!!!!!!!!!!!!!!!!!!!!!Contains forbidden word: %s" % word)
        else:
            return item

import pymongo

class MongoPipeline(object):

    collection_name = 'scrapy_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self):
        self.client.close()

    def process_item(self, item):
        self.db[self.collection_name].insert(dict(item))
        return item



class DropIfEmptyFieldPipeline(object):

    def process_item(self, item, crawlmycrown):

        # to test if only "job_id" is empty,
        # change to:
        # if not(item["job_id"]):
        if not(all(item.values())):
            raise DropItem()
        else:
            return item



class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            log.msg("Question added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item
