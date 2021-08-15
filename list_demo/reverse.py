def reverse_list(args):
    #return args[::-1]
    rlist=[]
    for i in args:
        rlist.insert(0,i)
    return rlist

limit = int(input("Enetr Limit for range"))
numbers=list(range(1,limit))
print(reverse_list(numbers))
