# re.findall helps to get a list of all matching patterns.
# it has no constraints of searching from start or end
import re
st="this is find all matching patterns and gives in a list and"
res=re.findall(r"and",st)
print(res)