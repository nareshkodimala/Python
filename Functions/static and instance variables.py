class Employee:
    comp_name="kelly"
    comp_cno=88102241
    def assign(self,id,na):
        self.idno=id
        self.name=na
    def display(self):
        print(Employee.comp_name)
        print(Employee.comp_cno)
        print(self.idno)
        print(self.name)
e1=Employee()
e1.assign(101,"Bunny")
e1.display()
e2=Employee()
e2.assign(102,"nani")
e2.display()
print(Employee.comp_name)
print(e1.idno)
print(e2.name)
print(e1.comp_name)
