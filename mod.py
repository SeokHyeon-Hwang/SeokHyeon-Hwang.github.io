# -*- coding: utf-8 -*-

def sum(a,b):
    return a+b

#def main():
#    val1=10
#    print(val1)

val2=11

#if __name__=='__main__':
#    main()

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
        
d=Dog('바우가')
d.sleep()
d.wag()
        