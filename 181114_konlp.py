

#%%
# konlpy 시작하기
from konlpy.tag import Kkma
kkma = Kkma()

kkma.sentences('안녕하세요! 오늘은 한글어 분석을 시작합니다')

#%%
# 명사분석
kkma.nouns('안녕하세요! 오늘은 한글어 분석을 시작합니다.')

#%%
# 형태소 분석
kkma.pos('안녕하세요! 오늘은 한글어 분석을 시작합니다')

#%%
# 한나눔 한글 엔진 사용해 보기
from konlpy.tag import Hannanum
hannanum=Hannanum()

#%%
# wordCloud 사용해보기
from wordcloud import WordCloud, STOPWORDS

import numpy as np
from PIL import Image

#%%
text = open('C:/Users/ktm/181108_python_exercise/python_class/alice.txt').read()
alice_mask = np.array(Image.open('./alice_color.png'))

stopwords=set(STOPWORDS) #불용어 처리
stopwords.add('said')

#%%


#%%
import matplotlib.pyplot as plt
import platform

#%%
# 한글 폰트 글꼴 설정
from matplotlib import font_manager, rc
path = 'C:/Windows/Fonts/malgun.ttf'

if platform.system() == 'Windows':
    font_name=font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system()=='Darwin':
    rc('font', family='AppleGothic')
else:
    print('Unknown System')
    
#%%
wc = WordCloud(background_color='white', max_words=2000, mask=alice_mask,
               stopwords=stopwords, contour_width=3, contour_color='steelblue')

#%%
# generate word cloud
wc.generate(text)
wc.words_

#%%
# 앨리스 그림 확인
plt.figure(figsize=(15,8))
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show

#%%
plt.figure(figsize=(15,8))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()