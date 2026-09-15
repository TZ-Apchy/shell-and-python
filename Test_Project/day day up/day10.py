# f1 = lambda i:1 if i <= 2 else f(i-1) * i
# print(f1(5))
# print(type(f1))

# def f2(x):
#     return x ** 2
#
# f3 = lambda x: x ** 2
#
# print(f2(3), type(f2))
# print(f3(3), type(f3))
# print((lambda x:x**2)(3))



# def map_list(fn, list1):
#     result = []
#     for item in list1:
#         i = fn(item)
#         result.append(i)
#     return result
#
# l = [1,2,3,4]
# def f4(x):
#     return x * 2
#
# # 这里的lambda表达式和上面的函数f4等价
# print(map_list(f4, l))
# print(map_list(lambda x: x * 2,l))
# print(map_list(lambda x: str(x),l))
# print(map_list(str,l))

