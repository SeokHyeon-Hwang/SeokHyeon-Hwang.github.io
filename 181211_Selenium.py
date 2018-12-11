# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:28:38 2018

@author: ktm
"""

#%%
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/ktm/python_exe/chromedriver.exe')

#%%
url = 'https://finance.naver.com/sise/'
driver.get(url)

#%%
selected_id = driver.find_element_by_id('KOSPI_now')
print(selected_id.text)

selected_id2 = driver.find_element_by_id('KOSPI_change')
print(selected_id2.text)
print(selected_id2.tag_name)
type(selected_id2.text)


#%%
from selenium import webdriver
driver = webdriver.Chrome('C:/Users/ktm/python_exe/chromedriver.exe')

url = 'https://finance.naver.com/sise/'
driver.get(url)

selected_class = driver.find_element_by_class_name('m8')
print(selected_class)
selected_class.click()


#%%
# 스타일난다 - bag 검색 - 가격 가져오기(1)
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import lxml

driver = webdriver.Chrome('C:/Users/ktm/python_exe/chromedriver.exe')
url = 'http://stylenanda.com/product/search.html?banner_action=&keyword=bag'
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')
soupA = soup.find_all('div', class_='name')

start=time.time()

end = time.time() - start
print('end time =', end)

#%%
print(soupA)
len(soupA)
for items in soupA:
    #print(items)
    inf_title
    
    
#%%
# 스타일난다 - 셔츠 검색 - 가격 가져오기(1)
 from selenium import webdriver
from bs4 import BeautifulSoup
import time
import lxml

driver = webdriver.Chrome('C:/Users/ktm/python_exe/chromedriver.exe')
url = 'http://stylenanda.com/product/search.html?keyword=%EC%85%94%EC%B8%A0&x=0&y=0&keyword_layer=&except_keyword='
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')
soup1 = soup.find('ul', class_='column4')
soup2 = soup1.find_all('p', class_='price')

#%%
# 스타일난다 - 셔츠 검색 - 가격 가져오기(2)
for items in soup2:
    price = items.text
    print(price)

#%%
# bgmstore.net 에서 해당 bgm 가져오기
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import lxml

driver = webdriver.Chrome('C:/Users/ktm/python_exe/chromedriver.exe')
url = 'https://bgmstore.net/search?page=0&qType=general&q=%ED%8C%8C%EB%9E%9C%EB%93%9C%20%ED%83%9D%ED%8B%B1%EC%8A%A4%201'
driver.get(url)

#%%

soup1 = BeautifulSoup(driver.page_source, 'lxml')
soup2 = soup.find_all('div', class_='d-flex align-items-center p-2 document-list-item false')
soup2

num=len(select_xpath)
print(num)
for items in select_xpath:
    items = select_xpath[0].click()
