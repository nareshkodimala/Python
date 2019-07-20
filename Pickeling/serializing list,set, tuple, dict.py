from typing import Optional, Any

my_friends=["bunny","sunny","chinnu"]
contacts={124,4575,47558}
nick_names=("nani","sam","anu")
details={"idno":101,"name":"naresh","salary":124580.00}
import pickle
file=open("contacts.txt","wb")
pickle.dump(my_friends,file)
pickle.dump(contacts,file)
pickle.dump(nick_names,file)
pickle.dump(details,file)
file.close()
print("data is written into file")

#data reading

import pickle
file=open("contacts.txt","rb")
res=pickle.load(my_friends,file)
print(res)
print(type(res))
res1=pickle.load(contacts,file)
print(res1)
print(type(res1))
res2=pickle.load(nick_names,file)
print(res2)
print(type(res2))
res3=pickle.load(details,file)
print(res3)
print(type(res3))
file.close()
print("thanks")