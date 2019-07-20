#
# a=input("enter:")
# def ad(a):
#     b = []
#
#     for x in a:
#         b.append(int(x))
#     return sum(b)
# # print(ad(a))
# if ad(a)<=9:
#     print(a)
# else:
#     a=ad
#
#



# no=int(input("enter number"))
# sum=0
# while no!=0:
#     r=no%10
#     no=no//10
#     sum=sum+r
# print("sum of numbers=",sum)

#example to write a program to display 1to 1 using while loop
# no=1
# while no!=11:
#     print(no,end="")
#     no+=1
# print("\n thanks")

#
# no=int(input("enter number"))
# reverse=0
# while no!=0:
#     r=no%10
#     no=no//10
#     reverse=(reverse*10)+r
# print("reverse order=",reverse)

#wap to read a number from user and print the sum of given digits
# number=int(input("enter a four digit number"))
# sum=0
# while number!=0:
#     r=number%10
#     no=number//10
#     sum=sum+r
# print("sum of numbers=",sum)


#wap to read a numbe r from user and print the sum of first and last digits from given numbers
# number=int(input("enter numbers"))
# first_no=number%10
# while number!=0:
#     last_no=number%10
#     number=number//10
# print("sum=",first_no+last_no)

#wap to read four digit number and print the sum of two middle digits
# number=int(input("enter fou"))
# first_no=number%10
# if number>=1000 and number<=9999:
#     sumof_all=0
#     while number!=0:
#         last_number=number%10
#         number=number//10
#         sumof_all+=last_number
#         print("sum of middle numbers=",sumof_all-(first_no+last_number))
#     else:
#         print("invalid number")
#


#
no=0
l=[5,10,15,20,25,30,35,40,40,45,50,55,60,65,70]
for x in range(1,6):
    for y in range(x):
        print(l[no],end=" ")
        no+=1
    print( )