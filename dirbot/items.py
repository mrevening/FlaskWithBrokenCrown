from scrapy.item import Item, Field


class Website(Item):
    description = Field()
    percentage = Field()
    count = Field()
