# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 13:10:53 2019

@author: ktm
"""

#%%
from bs4 import BeautifulSoup
import requests as req
import lxml

#%%
url = 'http://search.gmarket.co.kr/search.aspx?selecturl=total&sheaderkey=&gdlc=&SearchClassFormWord=goodsSearch&keywordOrg=%BF%A9%BC%BA%C0%C7%B7%F9&keywordCVT=%BF%A9%BC%BA%C0%C7%B7%F9%2C%BA%F2%BB%E7%C0%CC%C1%EE%BF%A9%BC%BA%C0%C7%B7%F9%2C%C1%DF%B3%E2%BF%A9%BC%BA%C0%C7%B7%F9&keywordCVTi=1&keyword=%BF%A9%BC%BA%C0%C7%B7%F9'
res = req.get(url)
#req.add_header('User-Agent', 'Mozilla/5.0')
html = res.content
soup = BeautifulSoup(html, 'lxml')
soup.prettify()

#%%
soup_item = soup.find('div', {'id' :'container'})
print(soup_item)

#%%
soup_it2 = soup_item.select('div.wrap' )[0]
print(soup_it2)

#%%
soup_it3 = soup_it2.find('div', {'id' : 'divAjaxContainer'})

print(soup_it3)