#!/usr/bin/env python3

def getInput():
    f_num = int(input('Enter first number'))
    s_num=int(input('Enter second number'))
    return f_num,s_num

def add():
    x,y=getInput()
    return x+y

def sub():
    x,y=getInput()
    return x-y

def mul():
    x,y=getInput()
    return x*y
def div():
    x,y=getInput()
    return x//y

def main():
    operation_all=[add,sub,mul,div]
    while (1):
        print('''
            1.Add
            2.Sub
            3.Mul
            4.Div
            5.exit
        ''')
        option=int(input("Enter your choice"))
        if option>4:
            break
        print(operation_all[option-1]())


if __name__=='__main__':main()