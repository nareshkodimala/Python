# for x in range (1,6):
#     for y in range(5,x,-1):
#         print(" ",end=" ")
#     for z in range(x):
#         print(z+1,end=" ")
#     print()
#
#
# #write a program to print  *
# #                         **
# #                        ***
# # for x in range(1,6):
# #      for z in range(5,x,-1):
# #          print(" ",end="")
# #      for z in range(x):
# #          print("*",end=" ")
# #      print()
#
# #wap to display  1
# #               1 2
# #              1 2 3
# for x in range(1,6):
#     for y in range(5,x,-1):
#         print(" ",end="")
#     for z in range(x):
#         print(z+1,end=" ")
#     print()
#
# #
#
#
# for x in range (5,0,-1):
#     for y in range(x):
#         print(y+1,end="")
#     print()
#
# #
a=6
for x in range(0,5,1):
    for y in range(x):
       print(" ",end=" ")
    for z in range(1,a):
       print(z,end=" ")
    a-=1
    print()

for x in range(0,5,1):
    for y in range(x):
        print("",end=" ")
    for z in range(5,x,-1):
        print(z+1,end="")
    print()

#############################
#

for x in range(1,8):
    if x==1 or x==7:
        print("*",*5)
    elif x==4:
        print("*",*4)
    else:
        print("*")

