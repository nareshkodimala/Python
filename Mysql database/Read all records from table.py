#read all records from table
# import sqlite3 as sql
# conn=sql.connect("database1.db")
# curs=conn.cursor()
# curs.execute("select * from employee")
# result=curs.fetchall()
# for x in result:
#     print(x)
# conn.close()

#script to read 1 record from table
IDno=int(input("enter IDNO:"))
import sqlite3 as sql
conn=sql.connect("databse1.db")
curs=conn.cursor()
curs.execute("select * from employee where IDno=?",(IDno,))
result=curs.fetchone()
if result:
    print("IDNO=",result[0])
    print("Name=",result[1])
    print("salary=",result[2])
else:
    print("invalid Idno")
conn.close()