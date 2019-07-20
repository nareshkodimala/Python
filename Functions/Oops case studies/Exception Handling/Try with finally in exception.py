# try:
#     import sqlite3 as sql
#     conn=sql.connect("bunny.db")
#     curs=conn.cursor()
#     try:
#         curs.execute("insert into employee values(101,'bunny',125800.2)")
#         conn.commit()
#         print("record is created")
#     finally:
#         conn.close()
#         print("connection is closed") #error
# print("thanks")


#raise exception
#to raise your exception from your own methods you need to use raise keyword
# def checkAge(age):
#     if age>=23 and age<=60:
#         return "valid age"
#     else:
#         raise  ValueError("invalid age")
# age=int(input("enter your age"))
# try:
#     res=checkAge(age)
#     print(res)
# except ValueError as ve:
#     print(ve)
# print("thanks")

#Assert Statments
def checkage(age):
    assert age>=23 and age<=60, "invalid age"
    return "valid age"
age=int(input("enter Your age"))
try:
    res=checkage(age)
    print(res)
except AssertionError as ae:
    print(ae)
print("thanks")