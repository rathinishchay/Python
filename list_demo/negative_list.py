#!/usr/bin/env python3

numbers=[1,2,3,4,5,-6,7,-8]

def negative_list(args):
    t=0
    for i in range(len(args)):
        if args[i] > 0:
            args[i]=-args[i]

negative_list(numbers)
print(numbers)