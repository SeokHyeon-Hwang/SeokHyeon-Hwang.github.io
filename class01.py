# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 11:21:43 2018

@author: ktm
"""

#%%
# 전역변수
result1=0

## first plus cal
def sum1(num):
    global result1 #함수 밖의 값 업데이트
    result1=result1+num
    return(result1)

def sub1(num):
    global result1
    result1=result1-num
    return(result1)

#%%
sum1(3)

#%%
sub1(2)


#%%
