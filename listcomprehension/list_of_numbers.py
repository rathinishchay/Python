items=[[1,2,3],1,1.0,2,3.12,True,False]

numbers = [str(i) for i in items if type(i)==float or type(i)==int]

print(numbers)
#o/p : ['1', '1.0', '2', '3.12']