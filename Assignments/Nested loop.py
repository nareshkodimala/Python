# # #using string in loop
# s1="Bunny"
# # print(s1)
# # print(s1[-1])
# # for c in s1:
# #     print(c)
# for x in s1[0::4]:
#     print(x,end="")
# print("\n---------------------")
# #print capital A to Z
# for x in range (65,91,1):
#     print(chr(x),end="")
# print("\n---------------------------------")
# #to print small a to z
# for s in range(97,123,1):
#     print(chr(s),end="")
# print("\n==================================")
# #to print capital A and small a
# for v in range (65,91,1):
#     print(chr(v),"",chr(v+32))
# print("\n=======================================")
# #print small a to z and Z to A
# counter=7
# for c in range(97,123):
#     print(chr(c),"",chr(c-counter))
#     counter+=2
# print("\n===========================================")
# #wap to writing a loop in another loop is caleed nested loop
# #nested loop
# for x in range(3):
#     for y in range(3):
#         print(y+1,end="")
#     print()
#
#
# #example program
# for x in range (5):
#     for y in range(5):
#         print(y+1,end="")
#     print()
#
# #example2 program:
# counter=1
# for a in range(3):
#     for y in range(3):
#         print(counter,end="")
#         counter+=1
#     print()
#
#
# #example3 program
# counter=65
# for x in range(5):
#     for y in range(5):
#         print(chr(counter),end="")
#         counter+=1
#     print()
#
# #example4 program
# #987
# #654
# #321
# counter=9
# for x in range(3):
#     for y in range(3):
#         print(counter,end="")
#         counter-=1
#     print()
#
# #example5 program
# for x in range(1,6):
#     for y in range(x):
#         print(y+1,end="")
#     print()
#
# #exaple6 program
# counter=1
# for x in range(1,5):
#     for y in range(x):
#         print(counter,end="")
#         counter+=1
#     print()
# # example7 program
# counter=65
# for x in range(1,6):
#     for y in range(x):
#         print(chr(counter),end="")
#         counter+=1
#     print()


#example8 program
#A
#AB
#ABC
#ABCD
#ABCDE
for x in range(1,6):
    counter=88
    for y in range(x):
        print(chr(counter),end="")
        counter+=1
    print()

#example9 program
for x in range(1,5):
    for y in range(x):
        print("*",end="")
    print()

#assignments
#read name from user and print
#B
#un
#nny
a=input("enter name:")
len=len(a)
for row in range(len):
    for col in range(row+1):
        print (a[col],end="")
    print()

#

no=0
a=(5,10,15,20,25,30,35,40,40,45,50,55,60,65,70)
for x in range(1,6):
    for y in range(x):
        print(a[no],end="")
        no+=1
    print()


#
a=1
for x in range(5):
    for i in range(x):
        print(a,end="")
        a+=1
        if a==10:
            a=0
    print()


def string_splosion(a):
    count=''
    for i in a[::1]:
        count+=i
        print(count,end="")
string_splosion(a)
