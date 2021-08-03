#!/usr/bin/env python3

def main():
    for i in inclusive_range(20):
        print(i,end=' ')
    print()

def inclusive_range(*args):
    numargs = len(args)
    start=0
    step=1
    stop=args[0]
    i=start
    while i <= stop:
        return i
        i += step
if __name__ == '__main__':main()
