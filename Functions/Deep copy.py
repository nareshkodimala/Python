import copy as cp
l1=[[10,20,],[25,30],[35,40]]
l2=cp.deepcopy(l1)
print("before")
print(l1)
print(l2)
#modification
l2[0][1]="nani"
print("after")
print(l1)
print(l2)