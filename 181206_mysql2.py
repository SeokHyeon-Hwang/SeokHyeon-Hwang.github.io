# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 12:13:24 2018

@author: ktm
"""

#%%

# Arnaconda prompt 명령어
# mysql -holcalhost -uroot -p
# use mydatabase;
# show database;
# show tables;
# describe customers;
# INSERT INTO [테이블명] (컬럼명1, 컬럼명2, 컬럼명3) VALUES (값1, 값2, 값3);
# select * from cistomers;

import mysql.connector

mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'qwer1234',
        database = 'mydatabase2')

mycursor = mydb.cursor()

#%%
# create DB
mycursor.execute('CREATE DATABASE mydatabase2')

#%%
# create TABLE
mycursor.execute('CREATE TABLE customers (id INT PRIMARY KEY , name VARCHAR(64), address VARCHAR(255))')
mycursor.execute('CREATE TABLE mytbl (id INT PRIMARY KEY, name VARCHAR(64), address VARCHAR(255))')
mycursor.execute('SHOW TABLES')
for x in mycursor:
    print(x)






#%%
# 03 DATA 3행을 추가한다. (INSERT INTO)
sql = 'INSERT INTO mytbl (id, name, address) VALUES (%s, %s, %s)'
val = [
       (1, 'Peter', 'Lowstreet4'),
       (2, 'Jhon', 'Lowstreet2'),
       (3, 'Mina', 'Lowstreet6'),
       (4, 'yoko', 'Hightreet1'),
       (5, 'Ain', 'Hightreet2'),
       (6, 'Rilly', 'Hightreet7'),
       (7, 'wang', 'Lowstreet9'),
       ]

mycursor.executemany(sql, val)
mydb.commit()


#%%
# 04. 데이터를 검색해서 가져온다. (SELECT * FROM ..)
sql = 'SELECT * FROM mytbl'
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
    print(x)
    
#%%
# 05. WHERE 절 - 조건을 걸어서 데이터를 일부 가져온다.
# SELECT * FROM [테이블명] WHERE 조건문
# SELECT * FROM [테이블명] WHERE name = 'Peter'
# SELECT * FROM [테이블명] WHERE address = 'Lowstreet4'
# SELECT * FROM [테이블명] WHERE name LIKE '%3' # 끝이 3으로 끝나는 것
# SELECT * FROM [테이블명] WHERE name LIKE '%3%' # 3을 중간에 포함한 것을 찾는다
# SELECT * FROM [테이블명] WHERE name LIKE '%3%' AND address LIKE '%3%'
# SELECT * FROM [테이블명] WHERE name in ('Peter', 'JAY2', 'KAY4')
# *는 해당하는 전체를 가져오겠다. 

#%%
sql = 'SELECT * FROM mytbl WHERE address LIKE "%2"'
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
    print(x)
    
#%%
# 06 ORDER BY - 어떤 열을 선택해서 정렬한다.
#SELECT * FROM mytbl ORDER BY name ASC
#SELECT * FROM mytbl ORDER BY name ASC, address DESC
#SELECT * FROM mytbl WHERE (name LIKE 'Peter%') AND (address='IOWA 3') ORDER BY name
#%%
sql = 'SELECT * FROM mytbl ORDER BY name ASC'
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#%%
sql = 'SELECT * FROM mytbl WHERE (address LIKE "%2") ORDER BY name'

mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
    print(x)
    
#%%
# 07. DELETE 명령 - (조건에 맞는) 데이터를 삭제한다
# DELETE FROM mytbl (테이블 전체 지우기)
# TRUNCATE TABLE
# DELETE FROM mytbl
# DELETE FROM
sql='DELETE FROM mytbl WHERE name = "yoko"'

mycursor.execute(sql)


# 삭제되었는지 확인
sql = 'SELECT * FROM mytbl'
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
    
#%%
# 08. DROP 명령 - 테이블을 삭제한다.
sql = 'DROP TABLE IF EXISTS customers'
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
    

#%%
# 09. UPDATE 명령 - 데이터를 수정한다.

sql = 'UPDATE mytbl SET name = %s WHERE name = %s'
val = ("hwang", "wang")

mycursor.execute(sql, val)

mydb.commit()
myresult = mycursor.fetchall()
mycursor.execute('SELECT * FROM mytbl')
for x in mycursor:
    print(x)


#%%
# 10. LIMIT 데이터를 제한된 수만큼 가져온다.

sql = "SELECT * FROM mytbl LIMIT 3"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)