class Employee:
    def assign(self,id,na):
        self.idno=id
        self.name=na
    def display(self):
        print(self.idno)
        print(self.name)
e1=Employee()
e1.assign(101,"nani")
e1.display()
e2=Employee()
e2.assign(102,"bunny")
e2.display()
#modification of exixting value
s1=input("enter name")
e1.name=s1
e1.display()