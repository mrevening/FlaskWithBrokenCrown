from scrapy.crawler import CrawlerProcess
from scrapy.conf import settings

from dirbot.spiders import crawlmycrown

settings.overrides.update({}) # your settings

crawlerProcess = CrawlerProcess(settings)
crawlerProcess.install()
crawlerProcess.configure()

crawlerProcess.crawl(crawlmycrown) # your spider here