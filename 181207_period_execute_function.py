# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 10:53:54 2018

@author: ktm
"""

# 주기적으로 실행되는 함수 만들기
#%%
## http://1byte.tistory.com/18
import threading

class AsyncTask:
    def __init__(self):
        pass
    
    def TaskA(self):
        print 'Process A'
        threading.Timer(1, self.TaskA).start()
        
    def TaskB(self):
        print 'Process B'
        threading.Timer(3, self.TaskB).start()
        
def main():
    print 'Async Function'
    at = AsyncTask()
    at.TaskA()
    at.TaskB()
    
if __name__ == '__main__':
    main()
