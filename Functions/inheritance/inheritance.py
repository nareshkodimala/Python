# #example on single inheritance
# class Employee:
#     comp_name="bunny"
# @staticmethod
#     def comp_info(self):
#         print("comp_name:",Employee.comp_name)
#     def assign(self,idno,name):
#         self.idno=idno
#         self.name=name
#     def display():
#         print("idno:",self.idno)
#         print("name:",self.name)
# class developr(employee):
#     def pa_salary(self,salary):
#         print("salary=",salary)
# d1=developr()
# # d1.assign(101,"nani")
# # d1.display()
# # d1.pay_salary(485000.20)
# # developr.comp_info()
#

#constrctor in single inheritance
#
# class A:
#     def __init__(self):
#         print("iam constrctor of class A")
#     def m1(self):
#         print("m1 of class A")
# class B(A):
#     def m2(self):
#         print("m2 of class b")
# x=B()
# x.m1()
# x.m2()

#perametarized constrctor in single inheritance
# class A:
#     def __init__(self,name):
#         self.name = name
#
#     def m1(self):
#         print("from class A",self.name)
#
#
# class B(A):
#     def m2(self):
#         print("from class B", self.name)
#
# x=B("bunny")
# x.m1()
# x.m2()

#Multi level inheritance
class A:
    def m1(self):
        print("m1 of class A")
class B(A):
    def m2(self):
        print("m2 of class B")
class C(B):
    def m3(self):
        print("m3 of class C")
x=C()
x.m3()
x.m2()
x.m1()
