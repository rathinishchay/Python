#!/usr/bin/env python3

def main():
    #x = [1, 2, 3, 4]
    #x=dict(id='1',name='nishchay')
    #add_numbers(**x)
    x=kitten()
    print(type(x),x)
def kitten():
    print('bowwh.')
    return dict(x=2,y=4)

def add_numbers(**kwargs):
    sum=0
    if len(kwargs) <= 0:
        print("No Input provided")
    else:
        for k in kwargs:
            print('Employee {} is {}'.format(k,kwargs[k]))
if __name__ == '__main__' : main()