class School:
    def student(self):
        name1=input("name")
        rollno1=int(input("rno:"))
        math1=int(input("math:"))
        eng1=int(input("eng:"))
        sci1=int(input("sci:"))
        sum1=math1+eng1+sci1
        per1=sum1/3
        name2 = input("name")
        rollno2 = int(input("rno:"))
        math2 = int(input("math:"))
        eng2 = int(input("eng:"))
        sci2 = int(input("sci:"))
        sum2 = math2 + eng2 + sci2
        per2 = sum2 / 3
        name3 = input("name")
        rollno3 = int(input("rno:"))
        math3 = int(input("math:"))
        eng3 = int(input("eng:"))
        sci3 = int(input("sci:"))
        sum3 = math3 + eng3 + sci3
        per3 = sum3 / 3
        name4 = input("name")
        rollno4 = int(input("rno:"))
        math4 = int(input("math:"))
        eng4 = int(input("eng:"))
        sci4 = int(input("sci:"))
        sum4 = math4 + eng4 + sci4
        per4 = sum4 / 3
        name5 = input("name")
        rollno5 = int(input("rno:"))
        math5 = int(input("math:"))
        eng5 = int(input("eng:"))
        sci5 = int(input("sci:"))
        sum5 = math5 + eng5 + sci5
        per5 = sum5 / 3
        print(name1,"roolno:",+rollno1,sum1,per1)
        print(name2,"roolno:",+rollno2,sum2,per2)
        print(name3,"roolno:",+rollno3,sum3,per3)
        print(name4,"roolno:",+rollno4,sum4,per4)
        print(name5,"roolno:",+rollno5,sum5,per5)
s1=School()
s1.student()