# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 11:17:38 2018

@author: ktm
"""

from __future__ import unicode_literals
import json
import codecs

class bricksetPipeline(object):
    def __init__(self):
        self.file = codecs.open('brickset.json', 'w', encoding='utf-8')
        
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    
    def spider_closed(self, spider):
        self.file.close()