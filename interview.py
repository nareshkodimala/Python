Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> if num > 1:
      for i in range(2, num):
         if (num % i) == 0:
            print(num, "is not a prime number")

            break
        else:
            print(num, "is a prime number")

    else:
        print(num, "is not a prime number")
