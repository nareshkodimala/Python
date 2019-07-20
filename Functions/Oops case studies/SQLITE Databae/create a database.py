#create a database in current folder
# import sqlite3 as sql
# conn=sql.connect("icii.db")
# print(conn)

#what is diff between string and raw string
# print("satya")
# print("sat\nya")
# print(r"sat\nhya")


#to create a database file in given loaction
# import sqlite3 as sql
# conn=sql.connect(r"F:\Softwares\Python\icici.db")
# print(conn)

#to create a table on database
# import sqlite3 as sql
# conn=sql.connect("bunny.db")
# curs=conn.cursor()
# curs.execute("create table employee(idno number,name text,salary real)")
# print("table is created")
# conn.close()
# print("connection is closed")


#example to create a student table
# import sqlite3 as sql
# con=sql.connect("naresh.db")
# curs=con.cursor()
# try:
#     curs.execute("create table student(roll no number,name text,marks number,grade text,percentage real)")
#     print("table is created")
# except sql.OperationalError:
#     print("table is avialble")
# con.close()
# print("connection closed")


#insert a record into employee table
# import sqlite3 as sql
# con=sql.connect("bunny.db")
# curs=con.cursor()
# curs.execute("insert into employee values(101,'bunny',18524.00)")
# con.commit()
# print("record is inserted")
# con.close()
# print("connection is closed")


#wap to read idno,name,salary of a employee and save into employee table.
id=int(input("IDNO:"))
na=input("NAME:")
sal=float(input("SALARY:"))
import sqlite3 as sql
con=sql.connect("bunny.db")
cur=con.cursor()
try:
    cur.execute("INSERT INTO employee (?,?,?) values (id,na,sal)")
    con.commit()
    print("record is inserted")
except sql.IntegrityError:
    print("IDNO is available")
con.close()
print("connection is closed")


#wap to read all records from employee table
# import sqlite3 as sql
# conn=sql.connect("bunny.db")
# curs=conn.cursor()
# curs.execute("select * from employee")
# result=curs.fetchall()
# print(result)
# conn.close()
# print("connection close")