import re

with open('lianxi.txt','r',encoding='utf-8') as f:
    content=f.read()

print("-"*30)

# # 提取lianxi.txt中的所有英文单词
# word_list=re.findall(r"[a-zA-Z]+",content)
# print(word_list)
#
# print("-"*30)
#
# # 提取lianxi.txt中的所有数字
# num_list1=re.findall(r"[0-9]+",content)
# num_list2=re.findall(r"\d+",content)
# print(num_list1,num_list2)
#
# print("-"*30)

# # 提取lianxi.txt中的所有单词和数字
# word_and_num_list1=re.findall(r"([a-zA-Z]+|\d+)",content)
# print(word_and_num_list1)
#
# word_and_num_list2=re.findall(r"([a-zA-Z]+)|(\d+)",content)
# for word_num in word_and_num_list2:
#     if word_num[0]:
#         print("单词：",word_num[0])
#     else:
#         print("数字：",word_num[1])

# print("-"*30)

# # 匹配ip地址
# ip_list=re.findall(r"\d+\.\d+\.\d+\.\d+",content)
# print(ip_list)

# # 非贪婪匹配
# reg_list1=re.findall(r'He.*(\d+).*emo$',content)
# # 贪婪匹配
# reg_list2=re.findall(r'He.*?(\d+).*emo$',content)
# print("非贪婪匹配reg_list1：",reg_list1,"\n贪婪匹配reg_list2：",reg_list2)
