fname = ['nishchay','bharat','abhi','shivani']
lname = ['rathi','rathi','rathi']

full_name=zip(fname,lname)

for i in full_name :
    print(i)

for first_name,last_name  in full_name :
    print(first_name + " " + last_name)

ls = [(1,1),(2,4),(3,9),(4,16)]
print(type(ls))
print(list(zip(*ls)))






