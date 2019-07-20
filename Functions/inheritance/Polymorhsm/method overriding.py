class first:
    def calc(self,no1,no2):
        print(no1+no2)
        print(no1-no2)
class second(first):
    def calc(self,no1,no2):
        super().calc(no1,no2)
        print(no1*no2)
        print(no1/no2)
class third(second):
    def calc(self,no1,no2):
        super().calc(no1,no2)
        print(no1%no2)
        print(no1**no2)
f1=first()
f1.calc(10,20)
s1=second()
s1.calc(100,2)
t1=third()
t1.calc(50,2)