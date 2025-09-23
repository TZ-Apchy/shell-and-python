# # search方法用于在整个字符串中搜索第一个匹配的值，如果匹配成功，则返回的是match对象，否则返回None
# # 语法：re.search(pattern,string,flags=0)
# import re
# pattern=r'\d\.\d+'
# s1="I study python3.10 every day，python2.10 I love you"
# s2="4.10python I study every day"
# s3="I study python every day"
# s1_search=re.search(pattern,s1)
# s2_search=re.search(pattern,s2)
# s3_search=re.search(pattern,s3)
# print(s1_search,s2_search,s3_search,sep="\n")
# print(s1_search.group(),s2_search.group(),s3_search,sep="\n")