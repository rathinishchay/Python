#!/usr/bin/env python3

#type conversion str
def string_demo():
    print('demo'+str(3))
    t=type(str(3))
    name,age=input("Enter name and age").split(",")
    print(age)

def withlogic_pal(*args):
    str=args[0]
    length=len(str)-1
    i=0
    flag=True
    while(i<length):
        if str[i]!=str[length]:
            flag=False
            break;
        i += 1
        length -= 1
    if flag==True:
        print("Palin")
    else:
        print("Not")
#Palindrome
def palindrome(*args):
    str=args[0]
    #reverse string
    rstr = str[::-1]
    if str==rstr:
        print('Palindrome')
    else:
        print("Not")
#string_demo()
#palindrome('mada')
withlogic_pal('madam')