# no=int(input("enter number:"))
# def prime(no):
#     for x in range(2,no):
#        if(no%2==0):
#            print(no,"not a prime")
#            break
#        else:
#            print(no,"is a prime")
# prime(no)
#


num = int(input("Enter a number: "))

def prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")

                break
        else:
            print(num, "is a prime number")

    else:
        print(num, "is not a prime number")
prime(num)

#to display giv en number even or odd
# no=int(input("enter number"))
# if no%2==0:
#     print(no,"even number")
# else:
#     print(no,"odd number")

#print l=(1,2,3,4) to 1234
# l=(1,2,3,4)
# for x in l:
#     print(x,end="")

            #find fibonacci number
# def fib(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         print(c)
# fib(5)
# num=int(input("enter num"))
def prime(num):

    if num > 1:
        for x in range(2,num):
            if(num % x)== 0:
                print(num," it is prime number")

                break
        else:
                print(num," prime number")
    else:
        print(num,"it is not prime number")
prime(num)