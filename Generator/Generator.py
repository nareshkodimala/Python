#generator
# def count():
#     no=5
#     yield no
#     no+=1
#     yield no
#     no+=1
#     yield no
#     no+=1
#     yield no
# i=count()
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


#example 2 on generator
def count(max):
    no=0
    while True:
        if no<max:
            no+=1
            yield no
        else:
            break
for x in count(10):
    print(x)