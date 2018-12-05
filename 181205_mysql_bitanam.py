# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 09:26:43 2018

@author: ktm
"""
# Arnaconda prompt 명령어
# mysql -holcalhost -uroot -p
# use mydatabase;
# show database;
# show tables;
# describe customers;
# INSERT INTO [테이블명] (컬럼명1, 컬럼명2, 컬럼명3) VALUES (값1, 값2, 값3);
# select * from cistomers;

#%% 01. DB 생성
# mysql 연결 프로그램인 mysql.connector
import mysql.connector

mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'qwer1234')

print(mydb)

mycursor = mydb.cursor()

# CREATE DATABASE DB명
mycursor.execute('CREATE DATABASE mydatabase')

mydb.commit()

#%% 02. DB 연결(특정 DB 지정)
import mysql.connector

mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'qwer1234',
        database = 'mydatabase')

mycursor = mydb.cursor()

# CREATE TABLE TABLE명
mycursor.execute('CREATE TABLE customers (name VARCHAR(64), address VARCHAR(255))')
mycursor.execute('CREATE TABLE customersA (name VARCHAR(64), address VARCHAR(255))')
mycursor.execute('CREATE TABLE mytable (id INT PRIMARY KEY, name VARCHAR(64), address VARCHAR(255))')
mycursor.execute('CREATE TABLE customersA (id INT PRIMARY KEY, name VARCHAR(64), address VARCHAR(255))')

mycursor.execute('ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')
mycursor.execute('ALTER TABLE customersA ADD COLUMN id INT PRIMARY KEY')
mycursor.execute('ALTER TABLE mytable ADD COL)

# SHOW TABLES;
mycursor.execute('SHOW TABLES')
# mycursor.execute('SHOW DATABASES')

type(mycursor)

mycursor.execute('DESCRIBE customers')
for x in mycursor:
    print(x)

# 데이터 넣기    
# INSERT INTO [테이블명] (컬럼명1, 컬럼명2, 컬럼명3) VALUES (값1, 값2, 값3);

# 쪼개서 넣기
sql = 'INSERT INTO customers (name, address) VALUES ( %s, %s)'
val = ('John', 'Highway 21')

sql = 'INSERT INTO mytable ( name, address) VALUES ( %s, %s)'
val = ('John', 'Highway 21')

mycursor.execute(sql, val)
mydb.commit()

sql = 'INSERT INTO customersA (id, name, address) VALUES (%s, %s, %s)'
val = [(5, 'Peter', 'Lowstreet4'),
       (6, 'Peter', 'Lowstreet3'),
       (8, 'Peter', 'Lowstreet5'),
       (9, 'Peter', 'Lowstreet8'),
       (11, 'Peter', 'Lowstreet7')
       ]

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, 'was inserted.')

## 데이터 확인
mycursor.execute('SELECT  * FROM customersA')

myresult = mycursor.fetchall()
for x in myresult:
    print(x)







