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
        yield i
        i += step
if __name__ == '__main__':main()

print("/\\/\\/\\")
print('\\\\')
#raw string print
print(r'Hello \n nishchay')
#printing emoji replace + with 000 at prefix with \
print('\U0001F603')