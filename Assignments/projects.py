# import string
# import random
# def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))
# id_generator()
# 'G5G74W'
# id_generator(3, "6793YUIO")
# 'Y3U'
result_str="";
for row in range(0,7):
    for column in range(0,7):
     if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
            result_str=result_str+"*"
     else:
       result_str=result_str+" "
       result_str=result_str+"\n"
print(result_str);