# # input any 4 digit number and reverce it
# Number = int(input("Please Enter any Number: "))
# Reverse = 0
# while(Number > 0):
#     Reminder = Number %10
#     Reverse = (Reverse *10) + Reminder
#     Number = Number //10
# print(Reverse)
# no="1234"
# for x in no[::-1]:
#     print(x,end="")
"================================================================="
#input any 4 digit number and reverce it
# num=(input("enter 4 digit number:"))
# s=len(num)
# if s==4:
#     for i in num[::-1]:
#         print(i,end="")
# else:
#     print("it is not a four digit number")
#
#
# #input any 4 digit no and find out the sum of first and last digit
# num=input("enter four digits number: ")
# count=0
# s=len(num)
# if s==4:
#     for i in num[::1]:
#         if i==num[0] or i==num[-1]:
#             count+=int(i)
#     print(count)
# else:
#      print("it is not a four digits number")
#
#

#input any four digit no and find out the sum of middle digits
# num=input("enter four digits number: ")
# count=0
# s=len(num)
# if s==4:
#     for i in num[::1]:
#         if i!=num[0] and i!=num[-1]:
#             count+=int(i)
#     print(count)
# else:
#      print("it is not a four digits number")


#input any 4 digit num and find out the difference of all digits
# num=input("enter four digits number: ")
# sub=0
# s=len(num)
# if s==4:
#     for i in num[::1]:
#         count=i
#         next=num[i+1]
#         sub+=int(count)-int(next)
#     print(count)
# else:
#      print("it is not a four digits number")


#print the multiplication table for any given number

# tab=int(input("enter table number: "))
# for i in range(1,20):
#     print(tab,"*",i,"=",tab*i)

#

string="my name is Naveen"
for i in string:
    print(i,end=",")


for i in range(10):
    if i==5:
        break
    else:
        print(i)
else:
    print("Here")


#
i=0
while i<3:
    print(i,end="")
    i+=1
else:
    print(0,end="")





