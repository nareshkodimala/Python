#Exception handling
# no1=int(input("enter no1:"))
# no2=int(input("enter no2:"))
# print("the sum of=",no1+no2)
# print("the div of=",no1/no2)
# print("the mul of=",no1*no2)
# print("the sub of=",no1-no2)
# print("thanks")

#example program on exception handling
# no1=int(input("enter no1"))
# no2=int(input("enter no2"))
# print("the sum=",no1+no2)
# try:
#     print("the div=",no1/no2)
# except ZeroDivisionError:
#       print("invalid input for division")
# print("the mul=",no1*no2)
# print("the sub=",no1-no2)
# print("thanks")


#single try block can have multiple excepts
# try:
#     no1=int(input("enter no1:"))
#     no2=int(input("enter no2:"))
#     print("the sum of=",no1+no2)
#     print("the div of=",no1/no2)
#     print("the mul of=",no1*no2)
#     print("the sub=",no1-no2)
# except ValueError:
#     print("enter numbers only")
# except ZeroDivisionError as zd:
#     print(zd)
# print("thanks")

#Nested try
#defining try and except in another try is called nested try
# try:
#     no1=int(input("enter no1"))
#     no2=int(input("enter no2"))
#     print("the sum of=",no1+no2)
#     try:
#         print("the div of=",no1/no2)
#     except ZeroDivisionError as zd:
#         print(zd)
#     print("the mul of=",no1*no2)
#     print("the sub of=",no1-no2)
# except ValueError:
#     print("thanks")

#try except else

# try:
#     no1=int(input("enter no1"))
#     no2=int(input("enter no2"))
#     print("the sum of=",no1+no2)
#     print("the div of=",no1/no2)
# except ValueError:
#     print("enter numbers only")
# except ZeroDivisionError as zd:
#     print(zd)
# else:
#     print("the mul of=",no1*no1)
#     print("the sub of=",no1-no2)
# print("thanks")

#finally
#the statemnts under the finally will execute in any situation if exception occured or not

# import sqlite3 as sql
# conn=sql.connect("sample.db")
# curs=conn.cursor()
# try:
#     curs.execute("insert into employee values(101,"bunny",15800.00))
#     conn.commit()
#     print("data inserted")
# except sql.OperationalError as oe:
#     print(oe)
# finally:
#     conn.close()
#     print("connection closed")
#print("thanks")
#not executed
