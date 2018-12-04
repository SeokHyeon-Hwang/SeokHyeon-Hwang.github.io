# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 11:22:24 2018

@author: ktm
"""

BOT_NAME = 'brickset'
SPIDER_MODULES = ['brickset.spider']
NEWSPIDER_MODULE = 'brickset.spider'
LOG_LEVEL='ERROR'
ITEM_PIPLINES = {'brickset.piplines.bricksetPipeline'}