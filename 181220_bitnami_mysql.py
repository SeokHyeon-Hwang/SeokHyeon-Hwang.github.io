# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 17:10:21 2018

@author: ktm
"""

#%%
# pip install pymysql

import pymysql

mydb = pymysql.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'qwer1234'
    )

# db가 이미 존재한다면
'''
import pymysql

mydb = pymysql.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'qwer1234',
        database = 'mydatabase'
    )
'''

#%%
# 커서 지정하기
mycursor = mydb.cursor()

#%%
mycursor

#%%
# db 만들기
sql = 'CREATE DATABASE mydatabase'

mycursor.execute(sql)

for x in mycursor:
    print(x)

#%%
# db 리스트 확인하기
sql = 'SHOW DATABASES'

mycursor.execute(sql)

for x in mycursor:
    print(x)

#%%
# db 사용하기
sql = 'USE mydatabase'

mycursor.execute(sql)

for x in mycursor:
    print(x)
    
#%%
# 사용 중인 db에 table 만들기
sql = 'CREATE TABLE auction (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), price VARCHAR(255), seller VARCHAR(255)  )'

mycursor.execute(sql)

for x in mycursor:
    print(x)
    
#%%
# table 리스트 확인하기
sql = 'SHOW TABLES'

mycursor.execute(sql)

for x in mycursor:
    print(x)

#%%
