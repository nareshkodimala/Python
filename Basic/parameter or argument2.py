def add(a=56,b=50):
    print(a)
    print(b)
    print("sum of=",a+b)
    print(id(a))
    print(type(a))
    print(type(b))
add()   #calling without passing values
add(5)  #calling with one value
add(b=10)  #calling function with named argument
add("Bunny","tech") #function with two arguments
add(a=10.25,b=2.5)  #calling function with named arguments
