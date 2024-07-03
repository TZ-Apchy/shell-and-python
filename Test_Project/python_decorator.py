# # 装饰器
# # 例1：
# def double(x):
#     return x*2
#
# def triple(x):
#     return x*3
#
# # 把函数当作参数传递
# def calc_number(func,x):
#     print(func(x))
#
# calc_number(double,3)
# calc_number(triple,4)


# # 例2：
# def get_multiple_fun(n):
#     def multiple(x):
#         return n*x
#     return multiple# 返回值是一个函数
#
# double=get_multiple_fun(2)
# triple=get_multiple_fun(3)
# print(double(4))
# print(triple(5))

# # 例3:
# def dec(f):
#     return 1
#
# @dec
# def double(x):
#     return x*2
#
# # 等价于double=dec(double)，相当于把double函数作为参数传递给了dec函数，最后把值又赋值给了和double函数同名的变量
# print(double)

# # 例4:
# import time
# def timeit(f):
#     def wrapper(x):
#         start=time.time()
#         ret=f(x)
#         print(time.time()-start)
#         return ret
#     return wrapper
#
# @timeit
# def my_func(x):
#     time.sleep(x)
#
# @timeit
# def other_func(x):
#     return x *2
#
# my_func(1)
# print(other_func(2))
