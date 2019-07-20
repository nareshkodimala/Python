# d1={"_id":201,"name":"bunny","salary":18500.20}
# from pymongo import MongoClient
# mc = MongoClient()
# mc.naresh.employee.insert_one(d1)
# print("data inserted")

# Script to insert document from user in mango db collection
idno=int(input("enter IDno"))
name=input("enter name:")
salary=float(input("enter salary"))
d1={"_id":idno,"name":name,"salary":salary}
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
mc=MongoClient()
try:
    mc.naresh.employee.insert_one(d1)
    print("data inserted ")
except DuplicateKeyError:
    print("Idno is available")
print("thanks")


#Script to read data from mongo DB
from pymongo import MongoClient
mc=MongoClient()
res=mc.naresh.employee.find()
for x in res:
    print(x)
    