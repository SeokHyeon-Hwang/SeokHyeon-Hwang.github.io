# -*- coding: utf-8 -*-

# 실행은 F9
class Cal:
    def __init__(self):
        self.result=0
    
    def add1(self,num):
        self.result=self.result+num
        return self.result
    
    def sub1(self,num):
        self.result=self.result-num
        return self.result
    
    def mul1(self,num):
        self.result=self.result*num
        return self.result
    
    def div1(self,num):
        self.result=self.result/num
        return self.result
    

    
cal1=Cal() # 계산기 만들기 & 공장 초기화
cal2=Cal()
cal3=Cal()

print(cal1.add1(2))
print(cal1.sub1(3))
print(cal1.div1(1))
print(cal2.add1(2))
print(cal3.add1(4))
print(cal3.mul1(3))

