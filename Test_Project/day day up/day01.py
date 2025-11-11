# # 字符串去重
# s="helloworlddjafaljfjfj"
#
# 方法一：字符串的拼接和not in
# new_s1=""
# for item in s:
#     if item not in new_s1:
#         new_s1+=item
#
# print(new_s1)
#
# # 方法二：使用索引和not in
# new_s2=""
# for i in range(len(s)):
#     if s[i] not in new_s2:
#         new_s2+=s[i]
#
# print(new_s2)
#
#
# # 通过集合去重
# new_s3=set(s)
# lst=list(new_s3)
# lst.sort(key=s.index)
# # print(lst)
# print("".join(lst))

# list1=list(s)
# list1.sort()
# list2=sorted(list1)
# print(list1,list2)
