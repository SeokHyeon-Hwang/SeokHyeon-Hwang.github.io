# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 12:14:41 2018

@author: ktm
"""

import scrapy
from scrapy.item import Item, Field

class bricksetItem(scrapy.Item):
    name = scrapy.Field()
    pieces = scrapy.Field()
    minifigs = scrapy.Field()
    image = scrapy.Field()