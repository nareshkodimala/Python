def outer(fun):
    a=int(input("enter no:"))
    def inner():
        fun()
        print(a)
    return inner()
def show():
    print("iam decorator")
inn=outer(show)
inn

# def c1(f1):
#     a=25
#     print("iam naresh")
#     def d1():
#         f1()
#         print(a)
#         print("years old")
#     return d1
# @c1
# def c2():
#     c=25
#     print("iam nani")
#     print("we are")
#     print(c)
# def d2():
#     print("ready for")
# c2()
# d2()
#

