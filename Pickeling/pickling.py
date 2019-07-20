#ex program to write a list into file
#list data
my_friends=['bunny','nani','naresh']
import pickle
file=open("contacts.txt","wb")
pickle.dump(my_friends,file)
file.close()
print("data written to file")

#ex program to read a list from file
import pickle
file=open("contacts.txt","rb")
res=pickle.load(file)
print(res)
print(type(res))