#example on Required and defalut argument
def add(no1,no2=53):
    print(no1+no2)
    print(id(no2))
    print(id(no1))
add(12)
add(10,25)
add(no1=5,no2=6)
add(no1="bunny",no2="nani")

def sub(no1,no2=42):
    print(no1-no2)
sub(10)
sub(12,25)
          
          


