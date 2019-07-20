# class Employee:
#     comp_name="bunny"
#     comp_cno=880199080
#     def assign(self,id,na):
#         self.idno=id
#         self.name=na
#     def display(self):
#         print(Employee.comp_name)
#         print(Employee.comp_cno)
#         print(self.idno)
#         print(self.name)
# e1=Employee()
# e1.assign(101,"nani")
# e1.display()
# e2=Employee()
# e2.assign(102,"naresh")
# e2.display()
# import pickle
# file=open("Employee.txt","wb")
# pickle.dump(e1,file)
# pickle.dump(e2,file)
# file.close()
# print("employee object written to file")

#read employee object from a file
class Employee:
    com_name="nani"
    com_cono=124536
    def assign(self,id,na):
        self.idno=id
        self.name=na
    def display(self):
        print(Employee.com_name)
        print(Employee.com_cono)
        print(self.idno)
        print(self.name)
import pickle
file=open("Employee.txt","rb")
data=pickle.load(file)
data.display()
data=pickle.load(file)
data.display()