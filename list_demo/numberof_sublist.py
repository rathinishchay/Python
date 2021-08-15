def numberof_sublist(args):
    count=0
    for i in args:
        if type(i) == list:
            count+=1
    return count

print(numberof_sublist([1,2,3,[1,7,9,4],[1,33]]))