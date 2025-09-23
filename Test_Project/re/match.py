# # match方法用于从字符串的开始位置进行匹配，如果起始位置匹配成功，则返回的是match对象，否则返回None
# # 语法：re.match(pattern,string,flags=0)

# import re
# pattern=r'\d\.\d+'
# str1="I study python3.10 every day"
# match_result1=re.match(pattern,str1)
# print(match_result1) # 开始位置没有匹配到，返回None
# str2="3.10python I study every day"
# match_result2=re.match(pattern,str2)
# print(match_result2) # 开始位置匹配成功，返回Match对象
# print("匹配值的起始位置：",match_result2.start())
# print("匹配值的结束位置：",match_result2.end())
# print("匹配区间的位置元组：",match_result2.span())
# print("待匹配的字符串：",match_result2.string)
# print("匹配的数据：",match_result2.group())