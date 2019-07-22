#re.search which  gives any postion of the given pattern string
# import re
# st="this program used for searching the given string"
# res=re.search(r"for",st)
# print(res)

#this is for retriving the given string
import re
st="this program for retriving the given string"
res=re.search(r"given",st)
print(res.group())

# in above example we can use start and end fun also