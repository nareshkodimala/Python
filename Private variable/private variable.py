#private method and private static variables and instance variables
# class Employee:
#     comp_name="bunny"
#     __comp_cno=8801999080
#     def __init__(self,idno,name):
#         self.__idno =idno
#         self.name=name
#     def display(self):
#         print("IDNO:",self.__idno)
#         print("NAME:",self.name)
#         self.__show()
#     def __show(self):
#         print("iam show")
# e1=Employee(101,"naresh")
# e1.display()
# e1._Employee__idno=102
# e1.name="nani"
# e1.display()
# print(Employee.comp_name)

class Employee:
    def assign(self,idno,name):
        self.__idno=idno
        self.__name=name
class Myemp(Employee):
    def display(self):
        print("idno:",self.__idno)
        print("name:",self.__name)
my=Myemp()
my.assign(101,"naresh")
my.display()













