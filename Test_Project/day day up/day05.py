# def get_max(a, b):
#     '''获取a和b中的最大值'''
#     v = a
#     if b > a:
#         v = b
#     # v = b if b > a else a
#     # 将return后面的值返回给外界
#     # return可以提前结束整个函数
#     return v

# i = get_max(5, 8)
# print(i)


# def set_age(age):
#     if type(age) != int:
#         return None    
#     if age < 0:
#         return None
#     print(age)

# set_age(2)


# def func(a, b):
#     return a + b, a - b

# i, j = func(3, 9)
# print(func(3, 9))
# print(type(func(3, 9)))
# print(f"i={i}, j={j}")