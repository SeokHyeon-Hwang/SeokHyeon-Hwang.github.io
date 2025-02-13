# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 12:18:56 2018

@author: ktm
"""



#%%
# library 불러오기
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
# mysql 실행
import mysql.connector

mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'qwer1234',
        database = 'mydatabase2')

mycursor = mydb.cursor()

#%%
# create TABLE
sql = 'CREATE TABLE auction2 (id INT AUTO_INCREMENT PRIMARY KEY , title VARCHAR(255), Dprice VARCHAR(255), price VARCHAR(255), seller VARCHAR(255), bcnt VARCHAR(255) )'
mycursor.execute(sql)

#%%
# 만들어진 Table 확인
sql = 'SHOW TABLES'
mycursor.execute(sql)
for x in mycursor:
   print(x) 


#%%
# auction2 테이블에 데이터 저장하기
num = len(soup_item)

for i in range(0,num):
    sql = 'INSERT INTO auction2 (title, Dprice, price, seller, bcnt) VALUE (%s, %s, %s, %s, %s)'
    val = (title[i], Dprice[i], price[i], seller[i], Bcnt[i])
    
    mycursor.execute(sql, val)
    mydb.commit()
    
#%%
## 저장한 데이터 확인
sql = 'SELECT * FROM auction2'
mycursor.execute(sql)

for x in mycursor:
        print(x)
