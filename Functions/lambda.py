fun=lambda:print("hello my dear commerade")
print(type(fun))
fun()
#function without parameter and without return in lambda
add=lambda:print(10+25)
add()
#function with parameter and without return in lambda
add=lambda no1,no2:print("the sum of",no1+no2)
add(10,30)
#function without parameter and with return in lambda
add=lambda:44+55
x=add()
print("the sum of",x)
#function with parameter and with return in lambda
add=lambda no1,no2:no1+no2
y=add(45,32)
print("the sum of",y)