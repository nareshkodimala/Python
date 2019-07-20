#scipt add salary in employee table
import sqlite3 as sql
conn=sql.connect("database1.db")
curs=conn.cursor()
curs.execute("select salary from employee")
res=curs.fetchall()
sum=0
for x in res:
    print(x[0])
    sum+=x[0]
print("total salary=",sum)
conn.close()
