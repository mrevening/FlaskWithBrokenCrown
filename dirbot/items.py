from scrapy.item import Item, Field


class Nazwy(Item):
    description = Field()
    type = Field()
    count = Field()
