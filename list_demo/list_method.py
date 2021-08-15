#!/usr/bin/env python3

list_str1 = ['apple','mango','kiwi']
#list assigment will make refrence to same list and cahging
#list is mutable can chage original list
list_str3=list_str1
print(id(list_str3))
list_str3.append('banana')
print(id(list_str1))
#-----------------------------------------------------------------

#copy function will create new list
list_str2=list_str1.copy()
#sort method will make changes in orginal list
list_str1.sort()
#sorted function won't make changes to orginal list
ls=sorted(list_str2)
print(list_str1)
print(list_str2)
print(ls)
print(list_str2)

print('---------------------------------------------------------------------------------------')
str='12344'
list1=['a','b','c']
list1[1]='d'
print(list1)
str[1]='3'
##pop method

