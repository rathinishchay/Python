def odd_even_sublist(args):
    odd=[]
    even=[]
    sub_list=[]
    for i in args:
        if i % 2==0 :
            even.append(i)
        else:
            odd.append(i)
    sub_list.append(odd)
    sub_list.append(even)
    return sub_list

def get_list():
    numbers = []
    num=int(input("Enter number"))
    numbers.append(num)
    while True:
        option=input("Do you wnat to add more number in list Y|N")
        if option=="Y" or option=="y":
            num = int(input("Enter number"))
            numbers.append(num)
        else:
            break

    return numbers

def main():
    list = get_list()
    print(odd_even_sublist(list))

if __name__ == '__main__':main()
