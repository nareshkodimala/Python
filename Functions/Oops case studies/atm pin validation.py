# a=input("enter pin no:")
# if len(a)==4:
#     if a=="1005":
#         print("enter withdraw")
#         amount=125000
#         withdrawl=int(input("enter amount"))
#         if withdrawl<=10000:
#             if withdrawl<amount:
#                 print("collect your cash",withdrawl)
#                 print("Current Balance",amount-withdrawl)
#             else:
#                 print("enter amount is more than Current Balance")
#         else:
#             print("day limit is 10000")
#     else:
#         print("invalid pin")
# else:
#     print("invalid pin")



a=input("enter pin no")
if len(a)==4:
    if a=="1005":
        print("enter withdrawl amount")
        amount =125000
        withdrawl=int(input("enter amount"))
        if withdrawl<=10000:
            if withdrawl<amount:
                print("collect your cash",withdrawl)
                print("current balance",amount-withdrawl)
            else:
                print("enter valid amount")
        else:
           print("day limit is 10000")
    else:
         print("invalid pin")
else:
  print("invalid pin")
print("Thank you")

