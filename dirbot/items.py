from scrapy.item import Item, Field


class Website(Item):
    description = Field()
    type = Field()
    count = Field()
