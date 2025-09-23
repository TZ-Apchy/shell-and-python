# # findall方法用于在整个字符串中搜索所有符合正则表达式的值，结果返回的是列表
# # 语法：re.findall(pattern,string,flags=0)
# import re
# pattern='\d\.\d+'
# s1="I study python3.10 every day，python2.10 I love you"
# s2="4.10python I study every day"
# s3="I study python every day"
# s1_findall=re.findall(pattern,s1)
# s2_findall=re.findall(pattern,s2)
# s3_findall=re.findall(pattern,s3)
# print(s1_findall,s2_findall,s3_findall,sep="\n")