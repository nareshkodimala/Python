class Employee:
    comp_name="naresh"
    comp_cno=45684
    def bunny(self,id,na,add):
        self.idno=id
        self.name=na
        self.address=add
    def display(self):
        print(Employee.comp_name)
        print(Employee.comp_cno)
        print(self.idno)
        print(self.name)
        print(self.address)
e1=Employee()
e1.bunny(101,"myprofile","my address")
e1.display()
print(Employee.comp_name)


