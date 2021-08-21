
l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]


''' 
    Below function definition is created without lambda and list comprehension.
    We are using zip function to grouping up element at same position in different lists.   
'''
# def average_finder(*args):
#     ls = list(zip(*args))
#     average=[]
#     for pair in ls:
#         average.append(sum(pair)/len(pair))
#     return average

''' 
    Below anonymous function definition created using lambda and list comprehension.
    We are using zip function to grouping up element at same position in different lists.   
'''

average_finder=lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]

average_list=average_finder(l1,l2)
print(average_list)


