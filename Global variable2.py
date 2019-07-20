def fun1():
    print("function1")
    a=10
    print(a)
def fun2():
    print("function2")
    global a
    a=60
    print(a)
print("Global variablr") 
a=56
print(a)
fun2()
print(a)
fun1()
print(a)
