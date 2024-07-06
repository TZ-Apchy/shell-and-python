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

# ----------------------------------------------- #

# # 原理讲解：
# # 需求：在函数执行前输入before，在函数执行后输出after
# # 例1：
# def func():
#     print("我是func函数")
#     value=(11,22,33,44)
#     return value
#
# def outer(origin):
#     def inner():
#         print("before")
#         res=origin() # 调用原来的func函数
#         print("after")
#         return res
#     return inner
#
# func=outer(func)
# # result=func()
# # print(result)
# print(func())

# 例2：优化
# python中支持特殊语法，在某个函数上方使用：@函数名
"""
@函数名
def xxx():
    pass
python内部会自动执行：函数名(xxx)，执行完之后，再将结果赋值给xxx
相当于执行了xxx=函数名(xxx)
"""

# def outer(origin):
#     def inner():
#         print("before")
#         res=origin() # 调用原来的func函数
#         print("after")
#         return res
#     return inner
# @outer # 相当于func=outer(func)
# def func():
#     print("我是func函数")
#     value=(11,22,33,44)
#     return value
#
# # func=outer(func)
# # result=func()
# # print(result)
# print(func())


# # 例3：多个函数实现，可以通过修改outer函数来达到目的，不用对每个函数单独修改
# def outer(origin):
#     def inner():
#         print("before")
#         res=origin() # 调用原来的func1、func2、func3函数
#         print("after")
#         return res
#     return inner
#
# @outer # 相当于func1=outer(func1)
# def func1():
#     print("我是func1函数")
#     value=(11,22,33,44)
#     return value
#
# @outer # 相当于func2=outer(func2)
# def func2():
#     print("我是func2函数")
#     value=(11,22,33,44)
#     return value
#
# @outer # 相当于func3=outer(func3)
# def func3():
#     print("我是func3函数")
#     value=(11,22,33,44)
#     return value
#
# # func=outer(func)
# # result=func()
# # print(result)
# print(func1(),end="\n\n")
# print(func2(),end="\n\n")
# print(func3(),end="\n\n")


# 例4：函数带参数的情况
def outer(origin):
    def inner(*args,**kwargs):
        print("before")
        res=origin(*args,**kwargs) # 调用原来的func1、func2、func3函数
        print("after")
        return res
    return inner

@outer # 相当于func1=outer(func1)
def func1(a1):
    print("我是func1函数")
    value=(11,22,33,44)
    return value

@outer # 相当于func2=outer(func2)
def func2(a2,b2):
    print("我是func2函数")
    value=(11,22,33,44)
    return value

@outer # 相当于func3=outer(func3)
def func3(a3,b3,c3):
    print("我是func3函数")
    value=(11,22,33,44)
    return value

# func=outer(func)
# result=func()
# print(result)
print(func1(1),end="\n\n")
print(func2(2,3),end="\n\n")
print(func3(4,5,6),end="\n\n")