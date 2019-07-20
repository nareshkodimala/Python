class Employee:
    def __init__(self,idno,name,salary=0.0):
        self.idno=idno
        self.name=name
        self.salary=salary
    def display(self):
        print("idno:",self.idno)
        print("name:",self.name)
        print("salary:",self.salary)
e1=Employee(101,"bunny",154625.25)
e1.display()
e2=Employee(102,"nani",156472.2)
e2.display()