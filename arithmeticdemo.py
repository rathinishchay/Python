#!/usr/bin/env python3

def main():
    a=4
    b=2
    
    x=division_demo(a,b)
    print(x)
#floating point
def division_demo(*args):
    return args[0]/args[1]

#integer point
def division_demo(*args):
    return args[0]//args[1]

if __name__ == '__main__':main()

