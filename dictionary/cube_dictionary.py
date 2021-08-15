#function return dictionary of number as key and value as cube of number
def cube_dictionary(num):
    cube_dict={}
    for i in range(1,num+1):
        cube_dict[i]=i**3

    return cube_dict

print(cube_dictionary(5))

print(__name__)