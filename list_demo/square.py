def square_list(args):
    number=[]
    for i in args:
        number.append(i**2)
    print(type(args))
    return number

print(square_list([1,2,3]))