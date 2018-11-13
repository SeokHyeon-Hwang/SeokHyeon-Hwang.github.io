# -*- coding: utf-8 -*-



#%%
# 리스트
dir([1,2,3])

#%%
# 튜플
dir((1,2,3))

#%%
# enumerate
litem=['body', 'foo', 'bar']
for i, name in enumerate(litem):
    print(i, name)
    
#%%
# sorted
sorted([3,1,2])

#%%
# sort()
a=[3,1,2]
result=a.sort()
print(result)

#%%
a

#%%
# tuple
tuple([1,2,3])

#%%
tuple('abc')

#%%
# zip
list(zip([1,2,3], [4,5,6]))

#%%
list(zip('abc', 'def'))

#%%
# 클래스 만들기
class Cookie:
    pass

#%%
# 객체 만들기
a=Cookie()
b=Cookie()

#%%
class FourCal1:
    def setdata(self, first, second):
        self.first=first
        self.second=second
                
    def add1(self,num):
        self.first=self.first+num
        self.second=self.second+num
        return self.first; self.second
    
    def sub1(self,num):
        self.first=self.first-num
        self.second=self.second-num
        return self.first; self.second
    
    def mul1(self,num):
        self.first=self.first*num
        self.second=self.second*num
        return self.first; self.second
    
    def div1(self,num):
        self.first=self.first/num
        self.second=self.second/num
        return self.first; self.second
    
        
#%%
a=FourCal1()
a.setdata(4,2)

a.add1(3)
a.sub1(1)

#%%
class FourCal:
    def __init__(self, first, second):
        self.first=first
        self.second=second
    def sum2(self):
        return self.first+self.second

#%%
a=FourCal(4,2)
a.sum2()


#%%
# 클래스 상속
class MoreFourCal(FourCal):
    pass

#%%
a=MoreFourCal(4,2)
a.sum2()

#%%
# 클래스의 변수
class Family:
    lastname='김'

#%%    
print(Family.lastname)


#%%
# 모듈
import sys
sys.path
sys.path.append('C:/module')

#%%
sys.path

#%%
import mod

#%%
# 클래스 만들기
class Human():
    def walk(self):
        print('걷는다.')
        
    def eat(self):
        print('먹는다.')
        
    def wave(self):
        print('손을 흔든다.')
        
class Dog():
    def walk(self):
        print('걷는다.')
    
    def eat(self):
        print('먹는다.')
        
    def wag(self):
        print('꼬리를 흔든다.')
        
#%%
person1=Human()
person2=Human()
person3=Human()

dog1=Dog()
dog2=Dog()

#%%
person1.walk()
person2.eat()
person3.wave()

dog1.wag()
dog2.eat()

#%%
# common class
class common():
    def walk(self):
        print('걷는다.')
        
    def eat(self):
        print('먹는다.')
        
class Human(common):
    def wave(self):
        print('손을 흔든다.')
        
class Dog(common):
    def wag(self):
        print('꼬리를 흔든다.')

#%%
# 클래스 객체 만들고, 메서드 만들기
person=Human()
person.walk()
person.eat()
person.wave()

dog=Dog()
dog.wag()

#%%
class Car():
    def run(self):
        print('차가 달립니다.')
        
    def stop(self):
        print('차가 멈춥니다.')
        
class Truck(Car):
    def load(self):
        print('짐을 싯습니다.')
        
class Taxi(Car):
    def sale(self):
        print('영업을 합니다.')
        
#%%
truck=Truck()
truck.stop()
truck.load()

taxi=Taxi()
taxi.run()
taxi.sale()

#%%
class General_Taxi(Taxi):
    pass

class Royal_Taxi(Taxi):
    pass

#%%
T1811=General_Taxi()
T1811.sale()

T1473=Royal_Taxi()
T1473.run()

#%%
# override : 자식 클래스에서 가져다 쓴다.
class common():
    def walk(self):
        print('걷는다.')
        
    def eat(self):
        print('먹는다.')
        
    def sleep(self):
        print('잠잔다.')
        
class Human(common):
    def wave(self):
        print('손을 흔든다.')
    def sleep(self):
        print('침대에서 잔다.')
        
class Dog(common):
    def wag(self):
        print('꼬리를 흔든다.')
    def sleep(self):
        print('소파에서 잔다.')
        
#%%
person=Human()
person.sleep()

dog=Dog()
dog.sleep()

#%%
# super class : 공통 매서드가 있을 때 부모의 것을 쓴다
class common():
    def walk(self):
        print('걷는다.')
        
    def eat(self):
        print('먹는다.')
        
    def sleep(self):
        print('잠잔다.')
        
    def greet(self):
        print('인사한다.')
        
class Human(common):
    def wave(self):
        print('손을 흔든다.')
    def sleep(self):
        print('침대에서 잔다.')
    def greet(self):
        self.wave()
        super().greet()
        
class Dog(common):
    def wag(self):
        print('꼬리를 흔든다.')
    def sleep(self):
        print('소파에서 잔다.')
    def greet(self):
        self.wag()
        super().greet()

#%%
person=Human()
person.greet()

dog=Dog()
dog.greet()

#%%
class common():
    def __init__(self, name):
        self.name=name
        
    def walk(self):
        print('걷는다.')
    def eat(self):
        print('먹는다.')
    def sleep(self):
        print('{} 잠잔다.'.format(self.name))
        
class Human(common):
    def wave(self):
        print('손을 흔든다.')
        
class Dog(common):
    def wag(self):
        print('꼬리를 흔든다.')
        
#%%
person=Human('철수가')
person.sleep()

dog=Dog('뽀삐가')
dog.sleep()

#%%
# try except

try:
    if value not in ['가위', '바위', '보']:
        raise ValueError('가위바위보 중의 하나의 값이어야 한다.')
except ValueError:
        print('잘못된 값을 입력했습니다. 다시 입력하세요.')
        
#%%
value=input()
value

#%%



     

#%%
# nltk
import nltk

#%%
from nltk.corpus import brown
brown.words()

#%%
# 토큰화
import nltk
sentence="""At eight o'clock on Thursday morning
Arthur didn't fell very good."""

#%%
tokens=nltk.word_tokenize(sentence)
print(tokens)

#%%
# 품사 태깅
tagged = nltk.pos_tag(tokens)
tagged[0:6]

#%%
# 구문 분석 트리 출력
from nltk.corpus import treebank
t=treebank.parsed_sents('wjs_0001.mrg')[0]
t.draw()

#%%
# KoNLPy 시작하기
from konlpy.tag import Kkma
kkma = Kkma()

kkma.sentences('안녕하세요. 오늘은 한글어 분석을 시작합니다.')

#%%
# 명
audt