# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:22:50 2018

@author: ktm
"""

#%%
from bs4 import BeautifulSoup
import requests as rq
import lxml

#%%
url = "http://browse.auction.co.kr/search?keyword={}&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk={}&acode=SRP_SU_0100&arraycategory=&encKeyword={}".format('여성의류', '여성의류', '여성의류')

res=rq.get(url)
html = res.content

soup=BeautifulSoup(html, 'lxml')

#%%
soup_item = soup.find_all('div', class_='section--itemcard')
num = len(soup_item)
num
title=[]
Dprice = []
price = []
seller = []
Bcnt = []
for i in range(0,num):
    # 상품명
    soup_title = soup_item[i].find('span', class_='text--title')
    print(soup_title)
    if soup_title is not None:
        title_text = soup_title.text
        title.append(title_text)
    else:
        title.append('')
    # 할인가
    soup_Dprice = soup_item[i].find('strong', class_='text--price_seller')
    if soup_Dprice is not None:
        Dprice_text = soup_Dprice.text
        Dprice.append(Dprice_text)
    else:
        Dprice.append('')
    # 판매가
    soup_price = soup_item[i].find('strong', class_='text--price_original')
    if soup_price is not None:
        price_text = soup_price.text
        price.append(price_text)
    else:
        price.append('')
    # 판매자
    soup_seller = soup_item[i].find('span', class_='text')
    if soup_seller is not None:
        seller_text = soup_seller.text
        seller.append(seller_text)
    else:
        seller.append('')
    # 구매량
    soup_Bcnt = soup_item[i].find('span', class_='text--buycnt')
    if soup_Bcnt is not None:
        Bcnt_text = soup_Bcnt.text
        Bcnt.append(Bcnt_text)
    else:
        Bcnt.append('')
        
#%%
# 가져온 리스트 출력
print(title)
print(Dprice);print(price);print(seller)

#%%