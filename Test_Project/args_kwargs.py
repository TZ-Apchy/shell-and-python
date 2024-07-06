# # *args允许传递任意数量的实参，并将其封装在一个名为args的元组中
# # **kwargs允许传递任意数量的关键字参数，并将其封装在一个名为kwargs的字典中

# # 例1:
# def adder(*args): # *args中args是一个占位符，也可以命名为其他的名称
#     result=0
#     for num in args:
#         result+=num
#     return result
#
# num1=[1,2,3] # num1=range(1,4)效果一样
# # num1=range(1,4)
# num2=(4,5,6)
# num3={7,8,9,10}
# print(adder(*num1, *num2, *num3)) # "*"号起到了解包的作用，如：这里把num1解包成了1,2,3三个参数

# # 例2：合并列表、元组
# list1=[1,2,3]
# list2=[4,5,6]
# list3=[7,8,9]
# tuple1=(1,2,3)
# tuple2=(4,5,6)
# tuple3=(7,8,9)
# print([*list1,*list2,*list3],list1+list2+list3,sep="\n") # list1+list2+list3会多占用一些内存
# print([*tuple1,*tuple2,*tuple3],list(tuple1)+list(tuple2)+list(tuple3),sep="\n")

# # 补充：dis模块通过反汇编分析字节码
# from dis import dis
# def work1(iter1,iter2):
#     return list(iter1)+list(iter2)
#
# def work2(iter1,iter2):
#     return [*iter1,*iter2] # 占用的内存小，相当于做了一些append的操作
#
# dis(work1)
# dis(work2)


# def f(**parameters):
#     print(parameters,type(parameters))
#     print(parameters['d'],parameters['e'])
#     # isinstance()函数来判断一个对象是否是一个已知的类型，类似type()
#     total=sum([item for item in parameters.values() if isinstance(item,int)]) # 列表生成式
#     print(total)
#
#
# f(a=1,b='b1',c=(1,'name',{'key':'value'}),d={'name':'join','age':33},e=1.5,f=2)

# # 合并字典
# a1={'name':'Tom','age':32}
# a2={'sex':'man'}
# a3={'city':'shanghai','name':'Join'}
# data={**a1,**a2,**a3} # a3中name的值会覆盖a1中name的值，放在后面的会覆盖放在前面的
# print(data)

# # 当有以下多种参数类型，位置参数，如a必须放在最前面，关键字参数如b放在*args和**kwargs中间
# def f(a,*args,b=0,**kwargs):
#     print(args,kwargs,b,a)
# f(1,2,3)
