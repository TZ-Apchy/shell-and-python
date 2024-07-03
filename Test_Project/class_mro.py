# # mro()：Method Resolution Order----方法解析顺序
# # 获取一个类的mro，如M类：M.__mro__或M.mro()

# # 例1：
# class A:
#     def say(self):
#         print("A")
# class M(A):
#     pass
#
# m=M()
# m.say()

# # 例2：mro顺序为M-->B-->A
# class A:
#     def say(self):
#         print("A")
# class B(A):
#     def say(self):
#         print("B")
# class M(B):
#     pass
#
# m=M()
# m.say()

# # mro顺序为F-->E-->D
# class D:
#     def __init__(self):
#         print("D")
# class E(D):
#     def __init__(self):
#         print("E")
# class F(E):
#     def __init__(self):
#         print(F.mro())
#         super().__init__() # 等价于super(F,self).__init__，会返回F类之后的那个类，即返回的是E类中的结果
# g=F()

# # 例3：mro顺序为M-->A-->B
# class A:
#     def say(self):
#         print("A")
# class B:
#     def say(self):
#         print("B")
# class M(A,B):
#     pass
#
# m=M()
# m.say()

# # 例4：mro顺序为M-->C-->A-->B
# class A:
#     def say(self):
#         print("A")
# class B:
#     def say(self):
#         print("B")
# class C(A):
#     pass
# class M(C,B):
#     pass
#
# m=M()
# m.say()

# # 例5：mro顺序为M-->C-->B-->A
# class A:
#     def say(self):
#         print("A")
# class B(A):
#     def say(self):
#         print("B")
# class C(A):
#     pass
# class M(C,B):
#     pass
#
# m=M()
# # print(M.__mro__) # 获取M类的mro，和下面等价
# print(M.mro())
# m.say()

