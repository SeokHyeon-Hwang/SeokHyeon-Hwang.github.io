# -*- coding: utf-8 -*-

#%%
# 분노의 질주 분석해 보기
import nltk
import matplotlib.pyplot as plt
import platform
import numpy as np

#%%
# from konlpy.tag import Twitter # 0.45 버전부터 변경.
from konlpy.tag import Okt

#%%
# 한글 폰트 설정
from matplotlib import font_manager, rc
path = 'C:/Windows/Fonts/malgun.ttf'
if platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system()=='Darwin':
    rc('font', family='AppleGothic')
else:
    print('Unknown System')


#%%
doc_ko = open('data/15_TheExtreme.txt').read()

#%%
doc_ko

#%%
# t= Twitter()
t=Okt()
tokens_ko = t.nouns(doc_ko)
tokens_ko

#%%
ko = nltk.Text(tokens_ko, name='분노의 질주')
print(len(ko.tokens)) # tokens의 수
print(len(set(ko.tokens))) # 유일한 tokens의 수
ko.vocab()

#%%
plt.figure(figsize=(12,6))
ko.plot(50)
plt.show()

#%% 불용어 처리
stop_words =[ '더', '말', '때', '눈', '또', '이', '그', '좀', '점', '것', '돈', '이제']

# ko = [each_word for each_word in ko if each_word not in stop_words]
new_ko = []
for one_word in ko:
    if one_word not in stop_words:
        new_ko.append(one_word)
        
#%%
new_ko= nltk.Text(new_ko, name='분노의 질주')
plt.figure(figsize=(12,6))
new_ko.plot(50)
plt.show

#%%
# 몇번이나 문서에서 언급이 되었을까?
new_ko.count('영화')

#%%
# 원하는 단어의 문서내 위치를 알 수 있음
plt.figure(figsize=(15,8))
new_ko.dispersion_plot(['영화', '액션', '시리즈', '분노'])

#%%
## 기타 참조 - konlp.pdf 참조
## new_ko.concordance('영화') # 주변부 단어 확인
## new_ko.collocations() # 어떤 단어들이 언어로 사용되었을까?
new_ko.collocations()

#%%
# 워드 클라우드 적용
from wordcloud import WordCloud, STOPWORDS

import numpy as np
from PIL import image

#%%
stopwords=set(STOPWORDS) # 불용어 처리
alice_mask = np.array(image.open('img/Draw_ca1.png'))

#%%
data = new_ko.vocab().most_common(150)

#%%
path = 'C:/Windows/Fonts/malgun.ttf'
wc = WordCloud(font_path=path, relative_scaling=0.2,
               background_color='while', mask=alice_mask).generate_from_frequencies(dict(data))

plt.figure(gifsize=(12,8))
plt.imshow(wc)
plt.axis('off')
plt.show()