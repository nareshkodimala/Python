#update to a table
idno=int(input("enter idno:"))
import sqlite3 as sql
conn=sql.connect("database1.db")
curs=conn.cursor()
curs.execute("select * from employee where idno=?",(idno,))
res=curs.fetchall()
if res:
    print("idno=",res[0])
    print("name=",res[1])
    #print("salary=",res[2])
    ans=int(int(input("to update press 1")))
    if ans==1:
        na=input("enter new name:")
        sal=float(input("enter sslary:"))
        curs.execute("update employee set name=?,salary=? where idno=?",(na,sal,idno))
        conn.commit()
        conn.close()
        print("updated")
    else:
        print("thanks")
else:
    print("invalid idno")
conn.close()
