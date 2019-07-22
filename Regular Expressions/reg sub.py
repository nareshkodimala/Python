#re.sub it helps to search pattern and replace with new sub string.
import re
st="world's best programming language is java"
res=re.sub(r"java","python",st)
print(res)
