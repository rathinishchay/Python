def common_element(list1,list2):
    output=[]
    for i in list1:
        if i in list2:
            output.append(i)
    return output

list1=[1,2,3,4]
list2=[1,4,5,9]
print(common_element(list1,list2))