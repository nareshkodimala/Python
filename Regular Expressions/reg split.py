#re.split this method helps to split string by the occurance of given pattern
# import re
# st="python"
# res=re.split(r"th",st)
# print(res)

#method split has another argument "maxsplit".it has defalut value as zero
import re
st="Programming"
res=re.split(r"m",st,maxsplit=1)
print(res)
