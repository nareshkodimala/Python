class Employee:
    comp_name="bunny"
    comp_cno=8801990
    @staticmethod
    def display():
        print(Employee.comp_name)
        print(Employee.comp_cno)
Employee.display()
