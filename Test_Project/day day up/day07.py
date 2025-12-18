# # 全局变量和局部变量
# i=6
# def f1():
#     i = 3

# f1()
# print(i)

# def f2():
#     "global定义全局变量"
#     global i
#     i = 7

# f2()
# print(i)
# print(f2.__name__) # 打印f2函数名
# print(f2.__doc__) # 打印函数f2的文档注释

# # 参数默认值只能从后往前设置
# def f3(name, age=0):
#     print(f"name = {name}, age = {age}")

# # 指定了age参数的值，则会使用指定的值
# f3("xiaoming", 18)
# # 没有指定age参数的值，则使用默认值
# f3("xiaohong")
# f3("xiaomao")


# def f4(a):
#     a = 0

# i = 6
# f4(i) # 相当于让a = i
# print(i)

# x = 5
# y = x
# y = 0
# print(x, y)

# list1 = [1, 2, 3]
# def f5(a):
#     a.append(6)
#     a = [8, 7, 4] # 给a重新赋了值，则不会改变list1的值
#     a.append(6)

# f5(list1)
# print(list1)