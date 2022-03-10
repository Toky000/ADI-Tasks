# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Task1Item(scrapy.Item):
    title = scrapy.Field()
    center = scrapy.Field()
    pi = scrapy.Field()
    links = scrapy.Field()
    pass
