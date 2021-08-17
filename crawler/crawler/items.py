# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Team1 = scrapy.Field()
    Team2 = scrapy.Field()
    Data = scrapy.Field()

class NextItem(scrapy.Item):
    Team1 = scrapy.Field()
    Team2 = scrapy.Field()
    Data = scrapy.Field()



