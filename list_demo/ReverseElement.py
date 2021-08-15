def reverseElement(args):
    rlist=[]
    for element in args:
        ls=list(element)
        str=""
        i=0
        for i in range(len(ls)):
            temp=ls.pop()
            str=str+temp
        rlist.append(str)
    return rlist
def get_list():
    list=[]
    ele = input("Enter number in  list")
    list.append(ele)
    while True:
        option=input("Do you want to add more element in list ...Y|N")
        if option== "Y" or option=="y":
            ele=input("Enter number in  list")
            list.append(ele)
        else:
            break
    return list

def main():
    ls=get_list()
    rlist=reverseElement(ls)
    print(rlist)

if __name__ == "__main__":main()