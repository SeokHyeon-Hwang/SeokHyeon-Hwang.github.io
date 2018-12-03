# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:19:56 2018

@author: ktm
"""

#%% 
#url에서 정보 불러오기
import requests as rq
url = 'https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=128641063'
res = rq.get(url)
print(res)

#%%
import requests as rq
url = "https://pjt3591oo.github.io"
res = rq.get(url)
print(res)


#%%
import requests as rq


def url_check(url):
    res = rq.get(url)

    print(res)

    sc = res.status_code

    if sc == 200:
        print("%s 요청성공"%(url))
    elif sc == 404:
        print("%s 찾을 수 없음" %(url))
    else:
        print("%s 알수 없는 에러 : %s"%(url, sc))


url_check("https://pjt3591oo.github.io/")
url_check("https://pjt3591oo.github.io//a")

#%% 03. URL정보를 가져온 후,  headers정보를 가져온다.

import requests as rq

url = "http://blog.naver.com/pjt3591oo"

res = rq.get(url)

print(res)
print(res.headers)


headers =res.headers
print(headers['Set-Cookie'])

for keys in headers:
    print(headers[keys])
    
#%% 04. 전체 헤더 정보를 가져오고 싶다. 
import requests as rq

url = "http://blog.naver.com/pjt3591oo"
res = rq.get(url)
print(res)
print(res.headers)
headers = res.headers

for keys in headers:
    print(headers[keys])


import requests as rq

url = "http://blog.naver.com/pjt3591oo"

res = rq.get(url)

print(res)

cookies = res.cookies
print(list(cookies))
print(dict(cookies))
print(tuple(cookies))

#%% 04. content, text를 이용하여 html 정보를 가져올 수 있다.
import requests as rq

url = "https://pjt3591oo.github.io/"

res = rq.get(url)

print(res.text)


#%% 04. content를 이용한 정보 가져오기
# 한글이 바이너리 형태로 나온다.
# 바이너리 형태로 된 것을 저장하고 하면 한글이 깨지는 것을 방지할 수 있다.
import requests as rq

url = "https://pjt3591oo.github.io/"

res = rq.get(url)

print(res.content)

#%% 04. content를 이용한 정보 가져오기
## 한글이 바이너리 형태로 나온다. 
## 바이너리 형태로 된 것을 저장하고 하면 한글이 깨지는 것을 방지해 줌. 
import requests as rq
url = "https://pjt3591oo.github.io/"
res = rq.get(url)
print(res.content)


#%% 구글 뉴스 쿼리 스트링 만들어 보기
#추천
import requests as rq
url = 'https://news.google.com/'
res = rq.get(url, params={'hl':'ko', 'gl':'KR', 'ceid':'KR:ko'})
res=rq.get(url)
print(res.url)

#%% 06. 구글 뉴스 쿼리 스트링 만들어 보기 
# https://news.google.com/?hl=ko&gl=KR&ceid=KR:ko
import requests as rq
url = "https://news.google.com/?hl=ko&gl=KR&ceid=KR:ko"
res = rq.get(url)
print(res.url)

#%% POST 방식 
import requests as rq
import json
url = "http://www.example.com"
res = rq.post(url, data=json.dumps({"key1": "value1", "key2": "value2"}))


print(res.url)

#%%
import requests as rq
url = "https://pjt3591oo.github.io/"
res = rq.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"})
print(res.url)


#%% 잘못된 URL
import requests as rq
url = "blog.naver.com/pjt3591oo"

try:
    res = rq.get(url)
except rq.exceptions.MissingSchema:
    print("MissingSchema 에러 발생")


#%%
from bs4 import BeautifulSoup
import lxml
import html5lib
html = """
<html>
<head>
<title>test</title>
</head>
</html>
"""
soup  = BeautifulSoup(html, 'lxml' )
# soup  = BeautifulSoup(html, 'html5lib' )
tag_title = soup.title
print(tag_title)


#%% 속성 가져오기
from bs4 import BeautifulSoup
import lxml
# html = res.text
html = """
<html>
<head>
<title class="c1">test</title>
<p id="p1"> p1 스트링 </p>
<p class="c1"> p1 class 지정1 </p>
<p class="c1"> p1 class 지정2 </p>
</head>
</html>
"""
soup  = BeautifulSoup(html, 'lxml' )
print(type(soup))
tag_p = soup.p
tag_title = soup.title
print(tag_p)
print(tag_title)
print(tag_p['id'])

print(tag_p.text)
print(tag_title.text)    # 해당 정보에 대한 tag와 tag사이의 내용 
print(tag_title.name)    # 해당 줄에 대한 tag명

print(tag_title['id'])

#%% 속성 가져오기
from bs4 import BeautifulSoup
import lxml
# html = res.text
html = """
<html>
<head>
<title class="c1">test</title>
<p id="p1">
<span> span part1</span>
<span> span part2</span>
</p>
<p class="c1"> p1 class 지정1 </p>
<p class="c1"> p1 class 지정2 </p>
</head>
</html>
"""
soup  = BeautifulSoup(html, 'lxml' )
a=soup.p.contents
print(a)
print(type(a))
#print(type(a))

#%%
a=soup.p.children
print(type(a))
for items in a:
    print(items)

#%%
from bs4 import BeautifulSoup

html = """
<html> 
<head>
<title>test site</title>
</head>
<body> 
<p>
<span>test1</span>
<span>test2</span>
</p> 
<div>
<p>
Hello, my name is Clarck.
Ohiyo, boku no namae wa Shinji desu.
</p>
<a href='https://google.com'>구글</a>
</div>
</body>
</html>
"""

soup = BeautifulSoup(html, 'lxml')

#tag_p_child = soup.p.children

#for child in tag_p_child:
#    print(child)

soup_div_child=soup.div.children

for child in soup_div_child:
    print(child)
    
#%%
from bs4 import BeautifulSoup

html = """<html>
<head><title>test site</title></head>
<body> 
<p><span>test1</span><span>test2</span></p> 
<div>
<p>p부분1</p> 
<p id='p2'>p부분2</p> 
<p>p부분3</p> 
</div>
</body></html>"""

soup = BeautifulSoup(html, 'lxml')

tag_span = soup.span
tag_span.next_sibling
tag_span.previous_sibling

p2 = soup.find('p', id='p2')
p2

p2.next_sibling.next_sibling

#%%  find_all( ), find() 
from bs4 import BeautifulSoup

html = """<html>
<head><title>test site</title></head>
<body> 
<p><span>test1</span><span>test2</span></p> 
<div>
<p class='c1'>p부분1</p> 
<p id='p2'>p부분2</p> 
<p class='c1'>p부분1</p> 

<p id='p3'>p부분3</p>
<p class='c2'>짜장면</p>
<p class='c2'>짬뽕</p>
</div>
</body></html>"""

soup = BeautifulSoup(html, 'lxml')

soup_p_all = soup.find_all('p')
soup_p_all

for items in soup_p_all:
    print(items)

soup_p_one = soup.find('p', id='p2')
soup_p_one

#%%
#1
soup_class_c2 = soup.find_all(class_='c2')
soup_class_c2

#%%
#2
soup_class_all = soup.find_all('p', id=False)
soup_class_all

#%%
#3
soup_p_id = soup.find_all('p', id=True)
soup_p_id

#%%  find_all( ), find() 
from bs4 import BeautifulSoup

html = """<html>
<head><title>test site</title></head>
<body> 
<p><span>test1</span><span>test2</span></p> 
<div>
<p class='c1'>p부분1</p> 
<p>p부분2</p> 
<p>p부분1</p> 
<p id='a1'><span>test3</span><span>test4</span></p> 
</div>
</body></html>"""

soup = BeautifulSoup(html, 'lxml')
p_tag = soup.find_all('p', limit=3)
p_tag
p0 = p_tag[0].find_all('span')
p0
for items in p0:
    #print(items)
    print(items.text)


#%%
#4
p_id_a1=soup.find('p', id='a1')
for item in p_id_a1.children:
    print(item.text)
    
#%%  find_all( ), find() 
from bs4 import BeautifulSoup

html = """<html>
<head><title>test site</title></head>
<body> 
<p><span>test1</span><span>test2</span></p> 
<div>
<p class='c1'>p부분1</p> 
<p>p부분2</p> 
<p>p부분1</p> 
<p id='a1'><span>test3</span><span>test4</span></p> 
</div>
</body></html>"""

soup = BeautifulSoup(html, 'lxml')
p_tag = soup.find_all('p', limit=3)
p_tag
p0 = p_tag[0].find_all('span')
p0
for items in p0:
    #print(items)
    print(items.text)


p_tag = soup.find_all('p', id="a1")[0].find_all("span")
p_tag

for items in p_tag:
    print(items.text)

#%%
from bs4 import BeautifulSoup

html = """<html>
<head><title>test site</title></head>
<body> 
<p><span>test1</span><span>test2</span></p> 
<div>
<p class='c1'>p부분1</p> 
<p>p부분2</p> 
<p>p부분1</p> 
<p id='a1'><span>test3</span><span>test4</span></p> 
</div>
</body></html>"""

soup = BeautifulSoup(html, 'lxml')
soup.find_all(['title', 'p'])

#%%  find_all( ), find() 
from bs4 import BeautifulSoup

html = """<html>
<head><title>test site</title></head>
<body> 
<p><span>test1</span><span>test2</span></p> 
<div>
<p class='c1'>p부분1</p> 
<p>p부분2</p> 
<p>p부분1</p> 
<p id='a1'><span>test3</span><span>test4</span></p> 
</div>
</body></html>"""

soup = BeautifulSoup(html, 'lxml')
p_tag = soup.find_all('p', limit=3)
p_tag
p0 = p_tag[0].find_all('span')
p0
for items in p0:
    #print(items)
    print(items.text)


p_tag = soup.find_all('p', id="a1")[0].find_all("span")
p_tag

for items in p_tag:
    print(items.text)

