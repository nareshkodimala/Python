# class A:
#     def assign(self,idno=0,name="",salary=18500.25):
#         self.idno=idno
#         self.name=name
#         self.salary=salary
#     def display(self):
#         print("idno:",self.idno)
#         print("Name:",self.name)
#         print("Salary",self.salary)
# x=A()
# x.assign(101)
# x.display()
# x.assign(102,"bunny",125.0)
# x.display()
# x.assign(103,"nani",125400.00)
# x.display()
#x.assign(idno=104,name="naresh")
#display()


#in python constractor overloading is also done implicitely
class A:
    def __init__(self, idno=0,name=None,salary=0.0):
        self.idno=idno
        self.name=name
        self.salary=salary
    def display(self):
        print("idno:",self.idno)
        print("nAme:",self.name)
        print("Salary:",self.salary)
A().display()
A(101).display()
A(102,"bunny",145000.02).display()
