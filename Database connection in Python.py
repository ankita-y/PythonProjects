import sqlite3

try:
    con = sqlite3.connect('emploeedetails.sqlite') # in case of connecting with Oracle system/root@localhost
    cursor = con.cursor()
    '''To table table in emploeedetails.sqlite'''
    #cursor.execute("create table employee(empid number,ename varchar(12),esal number(10,2))")
    #print("Table created successfully")
    '''To insert single record in table'''
    #cursor.execute("insert into employee values(100,'Jake',100)")
    '''To insert multiple record in table'''
    # sql = "insert into employee values(:empid,:ename,:esal)"
    # records = [(101,'Marry',500),(102,'Harry',700),(103,'Bravo',800)]
    # cursor.executemany(sql,records)
    '''To insert user input data in table'''
    while True:
        eno = int(input("Enter emp id: "))
        ename = input("Enter emp name: ")
        esal = float(input("Enter emp salary: "))
        sql = "insert into employee values(%d,'%s',%f)"
        cursor.execute(sql %(eno,ename,esal))
        option = input("Do you want to insert one or more records[yes|no]: ")
        if option.lower() =="no":
            con.commit()
            break
    #con.commit()
    print("Record inserted successfully")
except Exception as e:
    if con:
        con.rollback()
        print(e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()