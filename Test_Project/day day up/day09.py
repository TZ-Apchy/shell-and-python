# 元组解包
# a, b ,c = (1, 2, 3)

# def f1():
#     return 1, 2, 3

# result1 = f1()
# print(result1, type(result1), sep="\n")
# x, y, z = f1()
# print(x, y, z)

# # 任何可迭代类型都可以进行解包操作
# a, b, *c, d = 1, 2, 3, 4, 5, 6, 7
# # c是一个列表；会先给a、b、d赋值，其他的都是c
# print(a, b, c, d, sep="\n")

# # 列表解包
# a, b, *c, d = [1, 2, 3, 4, 5, 6, 7]
# print(a, b, c, d, sep="\n")

# # 字符串解包，此时a、b、c、d是字符串类型
# a, b, *c, d = "123456"
# print(a, b, c, d, sep="\n")

# # range类型可迭代对象
# a, b, *c, d = range(1, 9)
# print(a, b, c, d, sep="\n")

# # 字典类型可迭代对象，默认是对键进行解包
# a, *b = {'a': 1, 'b': 2, 'c': 3}
# print(a, b, sep="\n")

# # 使用字典值进行解包
# a, *b = {'a': 1, 'b': 2, 'c': 3}.values()
# print(a, b, sep="\n")

# # 键值都有进行解包，会得到a是一个元组，b是一个由键值元组组成的列表
# a, *b = {'a': 1, 'b': 2, 'c': 3}.items()
# print(a, b, sep="\n")

# def f2(a, b, c):
#     print(a, b, c, sep="-")

# list1=[1, 2, 3]
# f2(list1[0], list1[1], list1[2])
# f2(*list1)


# def f3(*args):
#     print(args)

# list2=[1, 2, 3, 4, 5]
# f3(*list2)


# def f4(**kwargs):
#     print(kwargs)

# dic1={'a': 1, 'b': 2, 'c': 3}
# dic2={'a': 1, 'b': 2, 'c': 3}.values()
# dic3={'a': 1, 'b': 2, 'c': 3}.items()
# print(dic1, dic2, dic3)
# f4(**dic1)
# print(*dic2)
# print(*dic3)

