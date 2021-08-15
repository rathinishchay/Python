list = [[i for i in range(1,4)] for j in range(3)]

print(list)

odd=[i for i in range(1,11) if i%2!=0]
even =[i for i in range(1,11) if i%2==0]

#List comprehension won't take elif but we can use mutiple nested else statments

odd_even_nested=[even if j%2==0 else odd if j%3==0 else [] for j in range(1,4)]

#odd_even_nested=[[i for i in range(1,11) if i%2==0] if j%2==0 else [i for i in range(1,11) if i%2!=0] for j in range(3)]

print(odd_even_nested)