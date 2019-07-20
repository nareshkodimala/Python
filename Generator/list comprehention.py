# #print even no in given list
l1=[10,12,15,25,20,21,23,42,46,45,2545,124,542,211,96,31]
# l2=[]
# for x in l1:
#     if x%2==0:
#         l2.append(x)
# print(l1)
# print(l2)
#
# print("list:",[x for x in l1 if x%2!=0])
#
# print("set:",{y for y in l1 if y%2==0})

num=[1,2,3,4,5,6,7,8,9,10]
# my_list=[]
# for n in num:
#     my_list.append(n*n)
# print(my_list)

# print("my_list=",[n*n for n in num])

# i want a (letter,num) pair for each letter in 'abcd' and each number in'0123'
# my_list=[]
# for x in "abcd":
#     for y in range(4):
#         my_list.append((x,y))
# print(my_list)

# print("my_list:",[(x,y)for x in 'abcd' for y in range(4)])

heros=['vijay','arjun','mahesh','charn','nani']
herions=['rashmika:','pooja','tamannah','kajal','samantha']

#i want to dict {'heros':'heroins'} for each name, hero in zip(heros,heroines)

# my_dict={}
# for heros,herions in zip(heros,herions):
#     my_dict[heros]=herions
# print(my_dict)
print({heros:herions for heros,herions in zip(heros,herions)if heros!='arjun'})

