def fun1():
    global a
    a=500
    print(a)
def fun2():
    print(a)
fun1()
fun2()
print(a)
