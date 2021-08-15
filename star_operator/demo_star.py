def sum(*args):
    total=0
    print(args)
    print(type(args))
    for num in args:
        total+=num
    return total

print(sum(1,2,3,))