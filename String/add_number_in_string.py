if __name__=='__main__':
    n=input("Enter string with numbers")
    total=0
    if n.isnumeric():
        for i in n:
           total+=int((i))
        print(total)
    else:
        print("Opps your string is not numeric string please enter correct string")