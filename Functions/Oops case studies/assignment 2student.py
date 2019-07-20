class school:
    def student(self):
        roll=int(input("roll no:"))
        name=input("student name:")
        eng=int(input("eng marks:"))
        math=int(input("math marks:"))
        sci=int(input("science marks:"))
        total=eng+math+sci
        print("total:",total)
        print("per:",total/3,"%")
# school().student()#unreffered
e=school()
e.student()
a=school()
a.student()