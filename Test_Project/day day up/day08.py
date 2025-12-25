# def f1(a, b, c):
#     return a + b + c

# result1=f1(4, 5, 6)
# print(result1)

# # 可变参数是可以传递任意数量的参数值
# def f2(*args):
#     # 在函数体内，可变参数args中保存了所有参数，是元组类型
#     # return args
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# result2=f2(4, 5, 6, 7)
# print(result2)

# # 最多只能有一个可变参数
# def f3(a, b, *args, c, d):
#     print(a)
#     print(b)
#     print(args)
#     print(c)
#     print(d)

# # 可变参数不支持关键字赋值
# # f3(a = 1, b = 2)
# # 调用函数时，可变参数之前，只用使用顺序实参，不能使用关键字实参
# # f3(a = 1, b = 2, 3, 4)
# # 调用函数时，可变参数之后，只用使用关键字实参，不能使用关顺序实参
# f3(1, 2, 3, 4, c = 5, d = 6)

# # **kwargs只能出现在参数列表的最后位置
# def f4(a, b, c, *args, d, **kwargs):
#     print(args)
#     # print(kwargs)
#     for k, v in kwargs.items():
#         print(f'{k} : {v}')

# # f4()
# # 可变参数后面的参数d必须使用关键字实参
# f4(1, 2, 3, 4, 5, 6, d=6, x=3, y=4)
# print("-"*10)
# f4(1, 2, 3, 4, 5, 6, x=3, d=6, y=4)
# print("-"*10)
# f4(1, 2, 3, 4, 5, 6, x=3, y=4, d=6)
