#lambda function with default arguments
add= lambda no1=0,no2=0,no3=0:print(no1+no2+no3)
add()
add(10,25,30)
add(25,10.25 ,10)
add(no1=12)
add(no1=15,no2=20,no3=-42)
print("===================================================")
#Wap to find big number out of two numbers using if else in lambda
big=lambda no1,no2:no1 if no1>no2 else no2
print("biggest no=",big(10,20))
print("big no",big(100,25))
print("=====================================================================")

#wap to find biggest number out of 3 numbers in lambda
big=lambda no1,no2,no3:no1 if no1>no2 and no1>no3 else no2 if no2>no3 else no3
print("big no =",big (3,2,1))
print("big no =",big (3,4,1))
print("big no =",big (3,4,5))

