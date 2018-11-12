# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 09:08:07 2018

@author: ktm
"""

class Contact:
    def __init__(self, nameP, phone_numP, e_mailP, addrP):
        self.name = nameP
        self.phone_number=phone_numP
        self.e_mail=e_mailP
        self.addr=addrP
        
    # 주소록에 생성된 사람의 정보를 출력
    def print_info(self):
        print('Name: ', self.name)
        print('Phone Number: ', self.phone_number)
        print('e-mail :', self.e_mail)
        print('address :', self.addr)
       
# create contact input puction
def set_contact():
        name=input('Name: ')
        phone_number=input('Phone Number: ')
        e_mail=input('e-mail: ')
        addr=input('addp: ')
        
        # create addr
        contact =Contact(name, phone_number, e_mail, addr)
        return contact
        
def print_menu():
    print('1. input contact :')
    print('2. output contact :')
    print('3. del contact :')
    print('4. exit')
    menu=input('sel Menu :')
    return int(menu)

# allList output function
def print_contact(ListA):
    for items in ListA:
        items.print_info()


# contact delete
def delete_contact(ListA, delname):
    for i,items in enumerate(ListA):
        if items.name == delname:
            del ListA[i]

def store_contact(ListA):
    f=open('contact_db.txt', 'wt')
    
    for items in ListA:
        f.write(items.name+'\n')
        f.write(items.phone_number+'\n')
        f.write(items.e_mail+'\n')
        f.write(items.addr+'\n')
    
    f.close()


def run():
    allList=[] #빈리스트 선언
    
    # 불러오기 함수
    
    
    while True:
    
        menu=print_menu()
        print('Our sel menu :', menu)
        
        if menu ==1:
            print('contact input')
            NewContact=set_contact()
            allList.append(NewContact)
        elif menu ==2:
            print('contact output')
            #NewContact.print_info()
            print_contact(allList)
            
        elif menu ==3:
            print('contact deleted')
            ## contact delete in the list
            name=input('the name we want delete is: ')
            delete_contact(allList, name)
        elif menu==4:
            print('exit')
            store_contact(allList)
            break
    #myContact=Contact( 'gildong', '010-1234-1234', 'qw1234@naver.com', 'Seoul')
    #myContact.print_info()
    
    #myFriend=Contact('soodol', '010-2221-1112', 'asd123@naver.com', 'Suwon')
    #myFriend.print_info()
    
if __name__=='__main__':
    run()