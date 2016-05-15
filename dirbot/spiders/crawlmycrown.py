from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings

from dirbot import settings
from dirbot.items import Website


class crawlmycrown(Spider):
    name = "crawlmycrown"
    allowed_domains = ["msbase.org"]
    start_urls = ['https://www.msbase.org/cms/benchmarking.json']

    def parse(self, response):
        sel = Selector(response)
        labels = sel.xpath('//tr[not(@*)]')
        items = []

        open('crawl_data.json', 'w').close()

        for data in labels:
            item = Website()
            item['description'] = data.xpath("td[1]/text()").extract()
            item['count'] = data.xpath('td[2]/text()').extract()
            item['percentage'] = data.xpath('td[3]/text()').extract()
            items.append(item)
        return items


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_FORMAT': 'json',
    'FEED_URI': 'result.json'
})

process.crawl(crawlmycrown)
process.start() # the script will block here until the crawling is finished