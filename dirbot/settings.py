# Scrapy settings for dirbot project

SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.Nazwy'

ITEM_PIPELINES = {#'dirbot.pipelines.FilterWordsPipeline': 1,
                  #'dirbot.pipelines.MongoPipeline':200,
                  #'dirbot.pipelines.DropIfEmptyFieldPipeline':100,
                  #'dirbot.pipelines.MongoDBPipeline':200
                  }
#FEED_EXPORTERS = {
#    'sqlite': 'dirbot.exporters.SqliteItemExporter',
#}



#MONGODB_SERVER = "localhost"
#MONGODB_PORT = 27017
#MONGODB_DB = "msdata"
#MONGODB_COLLECTION = "questions"
