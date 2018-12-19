# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:31:15 2018

@author: ktm
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 12:27:08 2018

@author: ktm
"""

import requests as rq
from bs4 import BeautifulSoup 
import lxml

url = "http://category.gmarket.co.kr//listview/List.aspx?gdsc_cd=300022173&ecp_gdmc=200002076&ecp_gdlc=100000083"
url

res = rq.get(url)
res.url
html = res.content
soup = BeautifulSoup(html, 'lxml')

#%% 타이틀 가져오기 
soup_item = soup.find('ul', class_='item_list type_list')
soup_item
soup_itemL = soup_item.find_all('li')
print(soup_itemL[1])

#%%
print(soup_item)


#%%
num = len(soup_itemL)
num
#%%
title = []
price_sales = []
free_fare = []
company = []
for i in range(0, num):
    # 상품명
    soup_title = soup_itemL[i].find("span", class_="title")
    print(soup_title)
    if soup_title is not None:
        title_txt = soup_title.text
        title.append(title_txt)
    else:
        title.append("")
        



    # 상품 가격
    
    
    soup_price = soup_itemL[i].find("strong")
    print(soup_price)
    if soup_price is not None:
        price_txt = soup_price.text
        price_sales.append(price_txt)
    else:
        price_sales.append("")

print(price_sales)
#%%
      
    # 회사명 
    soup_company = soup_itemL[i].find("span", class_="seller")
    print(soup_company)
    if soup_company is not None:
        title_txt = soup_company.text
        company.append(title_txt)
    else:
        company.append("")    


    # 배송비
    soup_free_fare = soup_itemL[i].find("span", class_="delivery")
    print(soup_free_fare)
    if soup_free_fare is not None:
        fare_txt = soup_free_fare.text
        free_fare.append(fare_txt)
    else:
        free_fare.append("")


print(title)
print(price_sales)
print(company)
print(free_fare)

#%%
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'qwer1234',
    database ='mydatabase'
   )


mycursor = mydb.cursor()
 
#%%
#create table>> insert data  by for 
#from 0,>> select 로 확인  
mycursor.execute('CREATE TABLE gmarket4 (id INT AUTO_INCREMENT PRIMARY KEY,title VARCHAR(255), price_sales VARCHAR(200), free_fare VARCHAR(200), company VARCHAR(200))')
mycursor.execute('SHOW TABLES')
for x in mycursor:
    print(x)
    
    
#%% STYLE.COM 융합 
# TABLE INPUT 
# 컬럼 이름: title price originPrice   
num = len (soup_item)

for i in range (0,num):
    sql = 'INSERT INTO gmarket4 (title ,price_sales, free_fare,company) VALUE (%s, %s, %s, %s)'
    val = (title[i], price_sales[i], free_fare[i], company[i])
    
    mycursor.execute(sql,val)
    mydb.commit()
#%% 확인 
sql = 'SELECT * FROM gmarket4'
mycursor.execute(sql)

for x in mycursor:
    print(x)
    
#%%테이블 드랍 
#mycursor = mydb.cursor()

#sql = "DROP TABLE auction2"

#mycursor.execute(sql)
#%% 테이블 보기 
mycursor.execute ('SHOW TABLES')
for x in mycursor:
    print(x)


#%% select 로 확인 
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM gmarket4')

myresult = mycursor.fetchall()

for x in myresult:
    print(x)    

#%%
#%%
import pandas as pd

print(title, len(title))
print(price_sales, len(price_sales))
print(free_fare, len(free_fare))
print(company, len(company))

title1 = pd.Series(title)
price_sales1 = pd.Series(price_sales)
price_ori1 = pd.Series(free_fare)
company_name = pd.Series(company)
#%% 
dat = pd.DataFrame({ "title" : title , 
                   "price_sales" : price_sales, 
                   "free_fare" : free_fare,
                   "company_name" : company },
    columns=['title','price_sales','free_fare', 'company_name'] )
dat

dat.to_csv("gmarket4.csv", index=False, encoding="utf-8")  # MAC 유저
dat.to_csv("gmarket4.csv", index=False, encoding="EUCKR")  # Window EXCEL 한글 볼 때    
