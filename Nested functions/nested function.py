#modifying outer function local variable in inner function
# def outer():
#     a=100
#     print(a)
#     def inner():
#         nonlocal a
#         a=200
#         print(a)
#     inner()
#     print(a)
# outer()

#creating a closure
#in this we can delete a fun name before del we have to assign a that function to one variable
#that variable holds all the info about del function like a copy
# def outer():
#     a=100
#     def inner():
#         print(a)
#     return inner()
# inn = outer()
# del outer
# inn

#passing function name as a parameter
def inc(no):
    no+=1
    return no
def dec(no):
    no-=1
    return no
def operation(fun,no):
    res=fun(no)
    print(res)
operation(inc,25)
operation(dec,25)
