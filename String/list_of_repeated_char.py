#!/usr/bin/env python3

def char_repeated(*args):
    temp={}
    str=args[0]
    length=len(str)
    i=0
    while i<length:
        key=str[i]
        if key in temp.keys():
            temp[key] +=1
        else:
            temp[str[i]]=1
        i+=1
    print(temp)
    all_values = temp.values()
    max_val=max(all_values)
    for key,value in temp.items():
        if value==max_val:
            print(key)
char_repeated('bbaaaacccccabc')

