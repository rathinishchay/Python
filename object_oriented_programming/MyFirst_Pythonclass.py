import mysql.connector

config = {
    'user':'demouser',
    'password':'9766116097Nbr@',
    'host':'dns1.nishchay.com',
    'database':'school'
}

# Insert data into database

try:
    con = mysql.connector.connect(**config)
    cursor=con.cursor()
    query=("Select * from parent")
    cursor.execute(query)
    for id ,fname,lname,email,mobile in cursor:
        print(f'{id}  :{fname} {lname} :{email} : {mobile}')

except mysql.connector.Error as err:
    print(err)
else:
    cursor.close()
    con.close()

