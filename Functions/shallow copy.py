import copy as cp
l1=[10,20,5,45,64]
l2=cp.copy(l1)
print(l1)
print(l2)
l2[2]=90
print(l1)
print(l2)
l1[-1]=99
print(l1)
print("==========================================================")
import copy as cp
l1=["bunny","nani"]
l2=cp.copy(l1)
print(l1)
print(l2)
l2[0]="love"
print(l2)

print("==========================================================================")
l1=[[10,20],[30,40],[50,60]]
import copy as cp
l2=cp.copy(l1)
print(l1)
print(l2)
l1[0][1]="bunny"
print(l1)
print(l2)
