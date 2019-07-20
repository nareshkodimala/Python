#script to insert user given data into employee table
idno=int(input("ID:"))
name=input("Name:")
sal=float(input("SAL:"))
import sqlite3 as sql
conn=sql.connect("database1.db")
curs=conn.cursor()
try:
    curs.execute("insert into employee values(?,?,?)",(idno,name,sal))
    conn.commit()
    print("data inserted")
except sql.IntegrityError:
    print("Idno is available")
finally:
    conn.close()
print("thanks")