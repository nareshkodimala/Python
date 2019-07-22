# self represents current class object
class Employee:
    def assign(e1,idno,name):
        e1.idno=idno
        e1.name=name
    def display(e1):
        print("idno:",e1.idno)
        print("name:",e1.name)
e1=Employee()
e1.assign(101,"naresh")
x=e1.display()

x=1
print(eval('x+1'))


