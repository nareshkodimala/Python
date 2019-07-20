#using map function in lambda
res=list(map((lambda x,y:x*y),[10,20,30,40,50],[5,10,15,20,25]))
print(res)
# using map function in lambda
result=list(map((lambda a,b,c,d:a+b+c+d),[10,20,60,40,50],[45,25,32,45,35],[1,2,3,4,5],[2,5,6,4,8]))
print(result)
print(id(-1))