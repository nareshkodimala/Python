#script to creat a db file in given path
# import sqlite3 as sql
# conn=sql.connect(r"C:\Users\Hi\Desktop\bunny.db.txt")
# print("database is created")
# conn.close()
# print("thanks")

#script to create a table
# import sqlite3 as sql
# conn=sql.connect("database1.db")
# curs=conn.cursor()#read and write
# try:
#     curs.execute("create table employee(idno number,name text,salary real)")
#     print("table is created")
# except sql.OperationalError as oe:
#     print(oe)
#
# finally:
#     conn.close()
# print("thanks")

#script to insert data into employee table
import sqlite3 as sql
conn=sql.connect("database1.db")
curs=conn.cursor()
try:
    curs.execute("insert into employee values(501,'anushka',154000.22)")
    conn.commit()
    print("data inserted")
except sql.IntegrityError:
    print("IDno is available")
finally:
    conn.close()
print("thanks")