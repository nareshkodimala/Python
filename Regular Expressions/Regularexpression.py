#this re.match() which finds only first matched string otherwise it gives None
# import re
# st="this is regular expresstion"
# result=re.match(r"this",st)
# print(result)
#

# which is gives matched name as it is by using group
# import re
# st="example of  print name only"
# result=re.match(r"example",st)
# print(result.group(0))

# example of start and end functions in regular expression
import re
st="example for start position of matching pattern in the string"
res=re.match(r"example",st)
#this strat fun gives first position of the given pattern string
print(res.start())
#this end fun gives first position of the given pattern string
print(res.end())


