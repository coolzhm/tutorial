# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()


class TutorialItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BiqugeItem(Item):
    name = Field()
    title = Field()
    link = Field()


class BiqugeContentItem(Item):
    content = Field()
