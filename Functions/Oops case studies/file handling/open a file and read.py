# file=open(r"C:\Users\Hi\Desktop\naresh.txt","r")
# data=file.read()
# print(data)
# file.close()

#example program to open an file and read number of characters
# file=open(r"C:\Users\Hi\Desktop\naresh.txt","r")
# data=file.read(6)
# print(data)
# file.close()

#example program on open a file and read first line from a file
# file=open(r"C:\Users\Hi\Desktop\naresh.txt","r")
# data=file.readline()
# print(data)
# file.close()

#example program to open a file and read all lines
# file=open(r"C:\Users\Hi\Desktop\naresh.txt","r")
# list_of_lines=file.readlines()
# print(list_of_lines)
# file.close()
#

#example to open a file and read user given line
# lno=5
# file=open(r"C:\Users\Hi\Desktop\naresh.txt",)
# lines=file.readlines()
# print(lines[lno-4])
# file.close()


#example program to create a file and write data into it
# file=open("nares.txt","w")
# file.write("hi this is bunny")
# file.close()
# print("Data written")

#to delete a file
# import os
# os.remove("nares.txt")

#
# file=open("naresh.txt","w")
# file.write("hi iam learning python")
# print("data wrtitten")
# file.close()


# example program to create a file and write data into it
# file=open("naresh.txt","a")
# file.write(" how are you")
# file.close()
# print("data written")


#check the given path or file available or not
# import os
# res=os.path.exists(r"F:\Softwares\nginx for load balancer chec.txt")
# if res:
#     file=open(r"F:\Softwares\nginx for load balancer chec.txt","r")
#     data=file.read()
#     print(data)
#     file.close()
# else:
#     print("file is not available")


#displaying the directory and all files nd folders
# import os
# dir_list=os.listdir(r"C:\Users\Hi\Desktop\REsumes")
# for x in dir_list:
#     print(x)

#displaying only files #not complted
# import os
# for x in dir_list:
#     if os.isfile(x):
#         print(x)

# import os
# for x in dir_list:
#     if not os.isfile(x):
#         print(x)

