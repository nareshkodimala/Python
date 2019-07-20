#function without parameter and without return
def add():
    print("the sum of=",10+25)
add()

#function with parameter and without return
def add(no1,no2,no3):
    print("the sum of =",no1+no2+no3)
add(10,20,30)
add("bunny","tech","sol")

#function without parameter with return
def add():
    a=10
    b=25
    return a+b
x=add()
print(x)
print("the sum of =",add())
print("the sum of ",x)

#another example on above program
def values():
    idno=102
    name="Bunny nani"
    salary=125456.20
    return (idno,name,salary)
b=values()
print(b)
print(type(b))
print([1])
