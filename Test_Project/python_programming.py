# import copy
# a = [1, 2, 3, 4, 5, [0], {'name': 3}]
# cy1 = a.copy()
# cy2 = copy.copy(a)
# cy3 = copy.deepcopy(a)
# # a.append(9)
# # a.insert(3,6)
# a[5].append(1)
# a[6].update({"age": 20})
# print(a)
# print(cy1, id(cy1), id(cy1[5]), id(a[5]))
# print(cy2, id(cy2), id(cy2[5]), id(a[5]))
# print(cy3, id(cy3), id(cy3[5]), id(a[5]))

# a = 10
# b = "hello"
# print(a is b)
# print(a is not b)

# a,b,c = (3,"hello",4.5)
# d,e,f = [3,"hello",4.5]
# [g,h,i] = (3,"hello",4.5)
# (j,k,l) = [3,"hello",4.5]
# m,n,o = 3,"hello",4.5
# print(a,type(a),b,type(b),c,type(c))
# print(d,type(d),e,type(e),f,type(f))
# print(g,type(g),h,type(h),i,type(i))
# print(j,type(j),k,type(k),l,type(l))
# print(m,type(m),n,type(n),o,type(o))

# del解除a与[1,2,3]的绑定关系
# a = [1,2,3]
# del a
# print(a)

# b = 3
# b **= 2
# print(b)
# 只有python2支持<>,表示不等于，如2<>3
# print(2 != 3)
# x = 34
# print(35 > x > 30, 30 < x < 35)
# a = 33
# b = "44"
# c = 55.62
# print(type(int(b)), a + int(b) + int(c))

# a = set('2')
# print(type(a))

# print(pow(2,3))
# import math
# print(math.pow(2,3))
# help(abs)
# help('sys')
# print()
# print("hello");x = 2;print(x)

# and中如果两条语句都为真时返回的是后面那个真的值，or中如果两条语句都为假时返回的是后面那个假的值
# and中如果两条语句都为假时返回的是前面那个假的值，or中如果两条语句都为真时返回的是前面那个真的值
# 其他情况根据整条语句的值对应返回，如整条语句为真，取真的值
# a = 3
# b = "4"
# c = 0.0
# d = 0
# print(a and b,type(a and b))
# print(c and d,type(c and d))
# print(a and c,type(a and c))
# print(c or d,type(c or d))
# print(a or b,type(a or b))
# print(a or d,type(a or d))

# 得到二进制、八进制、十六进制，转换后的都为字符串
# a = 10
# print(bin(a),type(bin(a)))
# print(oct(a),type(oct(a)))
# print(hex(a),type(hex(a)))

# & 位与（两个对应的位有一个为0则为0，都为1则为1）
# 10=0b01010,0b后面那个0是补上去的
# 20=0b10100
#    &:00000
# print(10 & 20)
# | 位或（两个对应的位有一个为1则为1，都为0则为0）
# 10=0b01010,0b后面那个0是补上去的
# 20=0b10100
#    |:11110=2^4+2^3+2^2+2^1=30
# print(10 | 20)
# ^ 位异或，也称半加运算（两个对应的位不同则为1，相同则为0）
# 10=0b01010,0b后面那个0是补上去的
# 20=0b10100
#    ^:11110=2^4+2^3+2^2+2^1=30
# print(10 ^ 20)
# << 位左移（相当于放大了对应的进制倍数，即在最右边添0）
# 0b1010 << 2，左移2位，相当于放大了2**2倍，即0b101000=40
# print(0b1010 << 2)
# >> 位右移（相当于缩小了对应的进制倍数，即在最右边抹去相应的位数）
# 0b111010 >> 2，右移2位，相当于缩小了，即0b1110=14
# print(0b111010 >> 2)
# 其他进制位左移和位右移要先转换成二进制再来操作
# print(6 << 1)
# print(0o101 << 1)
# ~ 按位求反（将数据二进制相应位取反，转换成10进制计算，如~x=-x-1）
# ~ 0b1010，相应位取反，即0b0101=5
# print(~ 0b1010)
# print(~ 0o101)
# print(~ 6)

# 计算优化
# a = 6
# b = 4
# c = 6
# d = 12  # 相当于8+4
# f = a * b
# g = c * d
# print(f, a << 2)  # f的值相当于a左移两位的结果
# print(g, (a << 3) + (a << 2))  # g的值相当于a左移三位加上a左移两位和的结果
# print(100 % 8, 100 & 7,sep='\n')

# 成员运算符（in 或 not in）
# a = [1,2,3]
# print(2 in a)
# print(4 not in a)

# 隐式换行
# print(2 +
#       3)

# input表示从键盘输入，输入的都是字符串（python3）,python2中输入的为数不是字符串，需用raw_input()
# a = input("输入的值为：")
# print(int(a) << 1)

# print(value,...,sep='',end='\n',file=sys.stdout,flush=False)
# import sys
# print(1,2,3,sep=',',end=' ')
# print(4,5,6,sep=',')
# print("hello",file=sys.stdout)
# print("hello",file=sys.stderr)

# 条件表达式  表达式1 if 真值表达式 else 表达式2
# a = 4
# b = a if a > 3 else -a
# print(b)

# del虽然解除了a与1的关系，但没能解除b与1的关系
# a = 1
# b = a
# c = a
# del a
# print(b,c)
# del b
# print(c)

# for i in range(1,11):
#     print(i)
# for j in range(1,11,3):
#     print(j)
# for k in range(5,0,-1):
#     print(k)
# for m in range(4,0):
#     print(m)

# python常用关键字
# import keyword
# print(keyword.kwlist)

# 不可变数据类型：当该数据类型的对应变量的值发生了改变，那么它对应的内存地址也会发生改变，对于这种数据类型，就称不可变数据类型
# 可变数据类型：当该数据类型的对应变量的值发生了改变，那么它对应的内存地址不发生改变，对于这种数据类型，就称可变数据类型
# 总结：不可变数据类型更改后地址发生改变，可变数据类型更改地址不发生改变
# 可变类型：列表、字典、集合
# a=[1,2]
# print(a, id(a))
# a.append(3)
# print(a, id(a))
# d1 = {'name': 'zhangsan', 'age': 20}
# print(id(d1))
# # d1["lan"]=2
# # d1['lan'] = d1.get('lan',2)
# d1.setdefault('lan', 2)
# print(d1, id(d1), sep="   ")
# # 不可变类型：数字、字符串、元组
# i = 1
# print(id(i))
# i = i+1
# print(id(i))
# a = [1, 2, 3, 4, 5 ,6, 7, 8]
# print(a[0:4])
# print(a[:4])
# b = [1, 2, 3, 4, 5, 6]
# b.insert(3, 10)
# print(b)

# 第一个"%"后面的内容为显示的格式说明，6为显示宽度，3为小数点位数，f为浮点数类型
# 第二个"%"后面为显示的内容来源，输出结果右对齐，2.300长度为5，故前面有一空格
# print("%6.3f" % 2.3)
# print("%6.3d" % 2.6)
# print("%+10x" % 10)
# print("%-5x" % -10)
# print("%05d" % 10)
# print("%.3f" % 10)
# pi = 3.1415
# print("pi的值是%s" % pi, type(pi))
# print("%10.*f" % (4, 1.2))

# print(3+2 << 1)
# b=a与b=a[:]的区别：b=a将两者指向同一个对象，而b=a[:]会创建一个新的与a完全相同的对象，但是与a并不指向同一对象
# is 与 == 区别：is 用于判断两个变量引用对象是否为同一个(同一块内存空间)， == 用于判断引用变量的值是否相等
# a = [1, 2, 3]
# b = a[:]
# c = a
# print(b)
# print(b is a, id(b), id(a))
# print(b == a)
# print(c is a, id(a), id(c))

# name = "aDa lovelace"
# print(name.title())  # 每个单词首字母大写
# print(name.upper())  # 每个字母都大写
# print(name.lower())  # 全部都小写
# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# print(full_name)
# print(f"Hello {full_name.title()}!")
# name1 = "Hello {} {}".format(first_name.title(), last_name.title())
# print(name1)
# print("python")
# print("\tpython")  # 制表符
# print("Languages:\npython\nc\njavascript")  # 换行符
# print("Languages:\n\tpython\n\tc\n\tjavascript")  # 换行符和制表符组合
# favorite_language = ' Python '
# print(f"Hello{favorite_language.rstrip()}Language")  # 删除favorite_language变量值的结尾空白
# print(f"Hello{favorite_language.lstrip()}Language")  # 删除favorite_language变量值的开头空白
# print(f"Hello{favorite_language.strip()}Language")  # 删除favorite_language变量值的开头和结尾空白

# a = 3
# print(f"{2*a}",type(f"{2*a}"))
# print({2*a},type({2*a}))
# print(2*a,type(2*a))

# 练习P21
# name = "eric"
# print(f"{name.title()},would you like to learn some Python today?")
# print(f"{name.lower()},would you like to learn some Python today?")
# print(f"{name.upper()},would you like to learn some Python today?")
# name = "albert einstein"
# quotes = "A persion who never made a mistake never tried anything new."
# print(name.title())
# print(quotes)
# print(f"{name.title()} once said,\"{quotes}\"")
# name = " albert einstein "
# print(name.title())
# print(name.title().lstrip())
# print(name.title().rstrip())

# 多个变量的赋值
# x,y,z = 1,2,3
# print(x,y,z)
# print(f"{x} {y} {z}")
# print(5+3,12-4,2*4,'%d' %(16/2),sep="\n")

# b=30
# a=100
# print(a)
# _a=5
# print(_a)
# if b!=a:
#     print(a,b)

# 二进制、八进制、十六进制转换成二进制
# c = 0b100
# d = 0o102
# e = 0xa
# print(int(c),int(d),int(e),type(int(c)))
# print(int('0b100', 2))
# print(int('0o102', 8))
# print(int('0xa', 16))

# c,d=0x1a,0x1A
# print(c,d)
# print(15*16+15)
# a=6.18e-1
# b=6.18E-1
# print(a,b)
# a=1+2j
# print(a)
# a=True
# print(a)
# a=100
# b=3
# print(a/b,a//b,a%b)
# a=12345
# print(a%100000)
# for i in range(1,5,2):
#     print(i)
# a=2**3
# print(a)

# print(0.2+0.1)
# print(2*0.2)
# print(7*0.2)
# print(4/2)
# universe_age = 14_000_000_000
# print(universe_age)

# a = (2, 3, 4)
# b = {2, 3, 4}
# print(a, type(a), b, type(b))

# list = ["a","b","c"]
# print(list[-1])
# motorcycles = ["honda","yamaha","suzuki"]
# print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles)
# motorcycles.append('yadi')
# print(motorcycles)
# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yadi')
# motorcycles.append('yamaha')
# print(motorcycles)
# motorcycles.insert(1,'luyuan')
# print(motorcycles)
# del motorcycles[1]
# print(motorcycles)
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)
# print(f"The last motorcycle I owned was a {popped_motorcycle.title()}.")
# print(motorcycles)
# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned.title()}.")
# print(motorcycles)

# motorcycles = ["honda","yamaha","suzuki","yamaha","yadi","yamaha"]
# print(motorcycles)
# motorcycles.remove("suzuki")
# print(motorcycles)
# too_expensive = 'yamaha'
# # motorcycles.remove(too_expensive)
# while "yamaha" in motorcycles:
#     motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"\nA {too_expensive.title()} is too expensive for me.")

# cars = ['bmw','audi','toyota','subaru']
# print(cars)
# # sorted临时排序默认小到大，可加reverse进行控制，不影响原来列表的顺序
# print(sorted(cars,reverse=True))
# print(cars)
# # sort永久排序，列表顺序被改变
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)
# # reverse对列表进行逆序排列，永久改变列表顺序
# cars.reverse()
# print(cars)
# # index()返回列表中元素的索引值
# print(cars.index("audi"))
# # len()可计算列表长度
# print(len(cars))
# # cars.clear()与del cars[:]都能删除列表中所有元素
# # cars.clear()
# del cars[:]
# print(cars)


# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)
#     print(f"{magician.title()},that was a great trick!")
#     print(f"I can't wait to see your next trick,{magician.title()}.\n")
# print("Thank you ,everyone.That was a great magic show!")

# for value in range(1,5):
#     print(value)
# # list()函数将range的结果直接转换成列表
# numbers = list(range(1,6))
# print(numbers,type(numbers))
# # 指定步长
# even_numbers = list(range(2,11,2))
# print(even_numbers,type(even_numbers))

# squares = []
# for value in range(1,11):
#     square = value**2
#     squares.append(square)
# print(squares,type(squares))
# # 列表解析
# squares = [value**2 for value in range(1, 11)]
# print(squares)

# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3], type(players[0:3]))
# print(players[-1], type(players[-1]))
# print(players[:3])
# print(players[2:])
# print(players[2:5])
# print(players[-3:])
# print(players[-3])
# print(players[1:4:2])
# print(players[:4:2])
# print(players[::])
# print(players[-5::1])
# print(players[-5::-1])
# print(players[-4:-5:-1])
# print(players[-4:-3:1])
# print(players[-4:-3:-1])
# print(players[-6::1])

# 复制列表使用切片[:]和不使用切片的区别：
# a = [1, 2, 3]
# b = a[:]
# c = a
# a.append(4)
# b.append(5)
# c.append(6)
# print(b, a)
# print(c, a)

# 元组（若想改变数组，可以重新定义整个数组）
# dimensions = (200, 50)
# for dimension in dimensions:
#     print(dimension, type(dimension))
# print(dimensions[0])
# print(dimensions[1])

# a = (3) # 这种表示没有报错
# b = (3,)
# c = 3
# print(a, b, c, type(a), type(b), type(c), sep='\n')

# age_0 = 22
# age_1 = 18
# print(age_0 >= 21 and age_1 >= 21)
# print(age_0 >= 21 or age_1 >= 21)
# age_1 = 22
# print(age_0 >= 21 and age_1 >= 21)
# print((age_0 >= 21) and (age_1 >= 21))
# age_0 = 18
# age_1 = 18
# print(age_0 >= 21 or age_1 >= 21)

# request_topping = ['mushrooms', 'onions', 'pineapple']
# print('mushrooms' in request_topping)
# print('pepperoni' in request_topping)

# input()是一个标准输入函数，返回类型为string
# age = int(input("请输入您的年龄："))
# if age < 4:
#     print("Your admission cost is $0.")
# elif age < 18:
#     print("Your admission cost is $25.")
# else:
#     print("Your admission cost is $40.")

# requests_toppings = ['a', 'b', 3]
# # 列表非空就返回True，否则返回False
# if requests_toppings:
#     for requested_topping in requests_toppings:
#         print(f"Adding {requested_topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")


# 字典
# alien_0 = {'color': 'green', 'point': 5}
# print(alien_0['color'])
# new_points = alien_0['point']
# print(f'you just earned {new_points} points!')
# 集合中有相同的值时，print的结果不会报错，结果只会显示一个
# c = {3, 3}
# # 字典中有两个相同的键时，print的结果并不会报错，但结果会显示后者
# a = {'b': 3,'b': 4}
# print(a,c)
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# 创建空字典
# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['point'] = 5
# print(alien_0)
# print(f"The alien is {alien_0['color']}.")
# alien_0['color'] = 'yellow'
# print(f'The alien is now {alien_0["color"]}.')

# 水平移动
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original x_position: {alien_0['x_position']}")
#
#
# def move():
#     if alien_0['speed'] == 'slow':
#         x_increment = 1
#     elif alien_0['speed'] == 'medium':
#         x_increment = 2
#     else:
#         x_increment = 3
#     alien_0['x_position'] = alien_0['x_position'] + x_increment
#     print(f"New x_position: {alien_0['x_position']}")
#
#
# move()
# alien_0['speed'] = 'fast'
# move()

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original x_position: {alien_0['x_position']}")
# alien_0['speed'] = 'fast'
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New x_position: {alien_0['x_position']}")

# 删除键值对
# alien_0 = {'color': 'green', 'point': 5}
# print(alien_0)
# del alien_0['point']
# print(alien_0)

# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }
# print(favorite_language)
# language = favorite_language['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# get方法获取键值对的值，它的第二个参数是可选的，没有时见返回None
# alien_0 = {'color': 'green', 'speed': 'slow'}
# point_value1 = alien_0.get('points', 'No point value assigned.')
# point_value2 = alien_0.get('points')
# speed_value = alien_0.get('speed', 'No point value assigned.')
# print(point_value1, point_value2, speed_value, sep='\n')

# a, b = (3, 5)
# print(type(a), a, b)
# user_0 = {
#     'usename': 'efermi',
#     'first': 'enrixo',
#     'last': 'fermi',
#     }
# print(user_0.keys(), user_0.values(), user_0.items(), type(user_0.items()), sep="\n")
# for key, value in user_0.items():
#     print(f"Key: {key}")
#     print(f"Value: {value}\n")

# def fun1():
#     return [lambda x : i * x for i in range(4)]
#
#
# print([m(2) for m in fun1()])

# a = 1
# a_b = []
#
#
# def sample_func():
#     a = 2
#     a_b.append(1)
#
#
# if __name__ == "__main__":
#     sample_func()
#     print(a, a_b)

# b = 6
# c = 6
# d = 6
# a = ((b + c)*d - 5)*6

# int = 3
# del int
# print(int(3.14))
# print(1.0 - 0.8)
# print(10/5)
#
# dic = {'tom': 97, 'lu': 98, 'jerry': 76}
# # 可以对键或值进行临时排序
# print(dic.keys(), sorted(dic.keys()))
# print(dic.values(), sorted(dic.values()))
# print(dic.items())
# for name, age in dic.items():
#     print(name, age, sep=":")
# for name1 in dic.keys():
#     print(name1)
# # 遍历字典会默认遍历所有的键
# for name2 in dic:
#     print(name2)

# # 集合中的每个元素都是独一无二的
# # dic = {'tom': 97, 'lu': 98, 'jerry': 98}
# # a = set(dic.values())
# # print(a)

# # 字典列表
# alien_0 = {'color': 'green', 'point': 5}
# alien_1 = {'color': 'yellow', 'point': 10}
# alien_2 = {'color': 'red', 'point': 15}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

# # 这样创建的外星人特征一样，不太实际
# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# print(f"Total number of aliens: {len(aliens)}")

# # 修改前三个外星人的特征
# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['point'] = 10
# for alien in aliens[:5]:
#     print(alien)
# print("...")

# # 字符串太长，可以考虑加引号换行
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
#     }
#
# print(f"You ordered a {pizza['crust']}-crust pizza "
#       "with the following toppings:")
# for topping in pizza['toppings']:
#     print("\t" + topping)

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")

# prompt = "If you tell us who you are, we can personalize the message you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}")

# # input输入的为字符串
# age1 = input("How old are you? ")
# print(age1, type(age1))
# age1 = int(age1)
# print(age1, type(age1))
# # 也可以利用int函数包裹在inout函数外面，效果一样
# age2 = int(input("How old are you? "))
# print(age2, type(age2))
# print(age2 >= 18)

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number +=1

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = input(prompt)
#     if message == "quit":
#         active = False
#     else:
#         print(message)

# import math
#
#
# def cal_vol(radius,height):
#     vol = math.pi * pow(radius,2) * height
#     return vol
#
#
# if __name__ == '__main__':
#     print(cal_vol(2,4))

# # floor返回数字的下舍整数
# import math
# print(math.floor(-45.73))
# print(math.floor(45.73))


# import math
# import argparse  # 1、导入argpase包
#
#
# def parse_arg():
#     parse = argparse.ArgumentParser(description='Calculate cylinder volume')  # 2、创建参数对象
#     parse.add_argument('radius', type=int, help='Radius of Cylinder')  # 3、往参数对象添加参数
#     parse.add_argument('height', type=int, help='height of Cylinder')
#     args = parse.parse_args()  # 4、解析参数对象获得解析对象
#     return args
#
#
# def cal_vol(radius, height):
#     vol = math.pi * pow(radius, 2) * height
#     return vol
#
#
# if __name__ == '__main__':
#     args = parse_arg()
#     print(cal_vol(args.radius, args.height))  # 5、使用解析对象.参数获取使用命令行参数

# for i in range(4):
#     print(i)
#     i = 2


# # 浮点数的操作
# # 1、将浮点数以四舍五入的方式进行取整，也可以四舍五入到小数点后几位
# a = 5.46
# b = 5.64
# c = 5
# print(round(a, 1), round(b, 1), round(c, 1))   # 是舍五入，保留的小数位数可选
# print(round(8.6))
# print(round(8.5))   #  这里结果为8

# # 2、向下取整
# # 方法一：使用 math 模块下的 floor(x) 方法
# import math
# d = 5.46
# e = 5.64
# f = 5
# print(math.floor(d), math.floor(e), math.floor(f))  # 为浮点数时向下取整，整数则不变

# # 方法二：使用 math 模块下的 trunc(x) 方法，截取整数部分并返回
# import math
# g = 5.46
# h = 5.64
# i = 5
# print(math.trunc(g), math.trunc(h), math.trunc(i))

# # 方法三：最直接的方法，将浮点数类型转化为整数类型，只会保留整数部分，即向下取整结果
# j = 5.46
# k = 5.64
# l = 5
# print(int(j), int(k), int(l))

# # # 3、向上取整
# # 使用 math 模块下的 ceil(x) 方法
# import math
# m = 5.46
# n = 5.64
# o = 5
# print(math.ceil(m), math.ceil(n), math.ceil(o))  # 为浮点数时则 向上取整，为整数时直接返回，不做任何更改

# print(0.1 + 0.2)
# a = (1, 2, 3)
# b = (2, 4, 5)
# print(b + a)   # 元组能相加，不能想减
# print(list(a))   # 元组转换成列表
# c = [1, 2, 3, 4]
# d = [3, 6]
# print(c + d)  # 列表能相加，不能相减
# e = {1, 2, 3, 4}
# f = {3, 6}
# print(e - f)  # 集合能相减，不能相加

# print(100 and 200)
# print(100 and 0)
# print(0 and 100)
# print(0 and 0)
# print(100 or 200)
# print(100 or 0)
# print(0 or 100)
# print(0 or 0)

# # return会将值存储到内存中，而print则是将结果回显到控制台
# def max_num(b, c):
#     if b > c:
#         # return b
#         print(b)
#     else:
#         return c
#
#
# max_num(9, 7)
# print(max_num(4, 7))

# import math
# import argparse  # 1、导入argpase包
#
#
# def parse_args():
#     parse = argparse.ArgumentParser(description='Calculate cylinder volume')  # 创建参数对象
#     parse.add_argument('--radius', default=2, type=int, help='Radius of Cylinder')  # 通过在参数名前加--，设置为可选参数，往参数对象添加参数
#     parse.add_argument('--height', default=4, type=int, help='height of Cylinder')
#     args = parse.parse_args()  # 4、解析参数对象获得解析对象
#     return args
#
#
# def cal_vol(radius, height):
#     vol = math.pi * pow(radius, 2) * height
#     return vol
#
#
# if __name__ == '__main__':
#     args = parse_args()
#     print(cal_vol(args.radius, args.height))  # 使用解析对象.参数获取使用命令行参数，这里都为可选参数

# import math
# import argparse  # 导入argpase包
#
# # 当通过设置required=True后，无论参数是否是可选参数，都必须输入
# def parse_args():
#     parse = argparse.ArgumentParser(description='Calculate cylinder volume')  # 创建参数对象
# 往参数对象添加参数
#     parse.add_argument('-r', '--radius', default=2, type=int, metavar='', required=True, help='Radius of Cylinder')
#     parse.add_argument('-H', '--height', default=4, type=int, metavar='', required=True, help='height of Cylinder')
#     args = parse.parse_args()  # 4、解析参数对象获得解析对象
#     return args
#
#
# def cal_vol(radius, height):
#     vol = math.pi * pow(radius, 2) * height
#     return vol
#
#
# if __name__ == '__main__':
#     args = parse_args()
#     print(cal_vol(args.radius, args.height))  # 使用解析对象.参数获取使用命令行参数，这里为必选参数，尽管有默认值

# # python中的循环终止
# # return：只能出现在定义的函数体中，作用为终止函数的执行，并返回函数的值
# def test1(n):
#     for i in range(n):
#         return i
#
#
# print(test1(10))
# # continue：退出当前循环，继续下一次的循环
# for i in 'python':
#     if i == 'h':
#         continue
#     print(i)
# # break：退出当前所在的循环体---例1
# for j in 'python':
#     if j == 'h':
#         break
#     print(j)
# # break：这里只退出了形参m所在的循环体，而k所在的循环体还会继续执行--例2
# for k in range(2):
#     print(k)
#     for m in 'python':
#         if m == 'h':
#             break
#         print(m)
# # exit：退出整个循环脚本
# for i in range(2):
#     # print(i, end="")  # end=''表示不换行输出
#     print(i)
#     for j in 'python':
#         if j == 'h':
#             exit()
#         print(j)
# print("end...")
# # pass：空语句，为了保持程序结构的完整性，简而言之pass就是占据一个位置，当你没有想好函数的内容时可以用pass来填充，使程序
# # 可以正常运行，并不会报错
# def sum1():
#     pass
#
#
# sum1()

# # 传递任意数量的实参：形参名*a中的星号让python创建一个名为a的空元组
# def b(*a):
#     print(a)
#     for i in a:
#         print(f"--{i}")
#
#
# b(1)
# b(1, 2)

# # 必须将定义中接纳任意数量实参的形参放到最后
# def e(c, *d):
#     print(f"{c} and {d}")
#     for i in d:
#         print(f"-{i}")
#
#
# e(1)  # 任意数量实参没传任何东西
# e(1, "tz")
# e(1, "tang", "zhi")
# print(e(c=1))  # 这里传的关键字实参

# # 任意数量的关键字实参
# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
#
#
# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')  # 关键字实参
# print(user_profile)

# def func(*args, **kwargs):
#     print("args:", args, "  kwargs:", kwargs)
#
# func(4, 5)
# func(name="Tom", age=20)
# func(4, 5, name="Tom", age=20)

# # 类和对象
# class A():
#     def run(self):
#         print("running")
#     def run2(self,c):
#         c.run()
#         c.run()
#
#
# class B(A):
#     def run(self):
#         print("run - run")
#
#
# class C(A):
#     def run(self):
#         print("run + run")
# a= A()
# b = B()
# c = C()
# a.run()
# b.run()
# c.run()
# b.run2(a)
# b.run2(b)
# b.run2(c)

# class Person():
#     def __init__(self, age):
#         self.age = age
#     # 构造方法
#     def __new__(cls, age):
#         if age > 50:
#             return None
#         else:
#             return object.__new__(cls)
#     def say_hi(self):
#         print(f"我今年{self.age}岁了")
#
# # obj2 = Person(51)  # 会报错
# # obj2.say_hi()
# obj1 = Person(5)
# obj1.say_hi()

# class Person():
#     def say_hi(self):
#         print("我是人类")
#
# class A:
#     def say_hi(self):
#         print("I am A")
#
# # 就近原则
# class B(A,Person):
#     pass
#
# obj1 = B()
# obj1.say_hi()

# class Person():
#     def __init__(self, name):
#         self.name = name
#
#     def say(self, *args):
#         if len(args) == 1:
#             return self.say1(*args)
#         if len(args) == 2:
#             return self.say2(*args)
#     def say1(self, i):
#         print(i)
#
#     def say2(self, i, j):
#         print(i + j)
#
#
# obj1 = Person("Tom")
# obj1.say(10)
# obj1.say(10, 20)

# class Dog():
#
#     def __init__(self, name, age):  # 初始化属性name和age
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(f"{self.name} is now sitting.")
#
#     def roll_over(self):
#         print(f"{self.name} rolled over!")
#
# d = Dog("tom", 10)
# d.sit()
# # print(d.name)  # 表示调用当前对象的name属性
# d.roll_over()
