class Sbi:
    name="naresh"
    typeofaccount="savings"
    accountnymber=123456789
    Balance=45640000
    b=int(input("enter account number"))
    def account(self):
        if Sbi.b ==123456789:
            a=input("withdrawl/deposit:").upper()
            if a == "WITHDRAWL":
                Amount = int(input("enter the withdrawl amount:"))
                if Amount < Sbi.Balance:
                    Balance= Sbi.Balance-Amount
                    print("u can collect ur cash:",Amount)
                    print("remaining balance",Balance)
                elif Amount == Sbi.Balance:
                    print("sorry u need to maintain atleast 1000rs")
                elif Amount > Sbi.Balance:
                    print("insufficient funds")
                else:
                    print("please enter valid input")
            elif a=="Deposite":
                amount=int(input("enter the deposite amount:"))
                Balance = Sbi.Balance+amount
                print("ur balance",Balance)
            else:
                print("please enter proper input")

        else:
            print("invalid account number")
e=Sbi()
e.account()