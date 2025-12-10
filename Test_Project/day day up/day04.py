# def good_morning():
#     say_hi()
#     print("Good morning")

# def say_hi():
#     print("Hello")

# good_morning()

# 三个单引号或双引号注释可以指明函数的用途，在调用时就会有对应的说明提示
def line(width, char: str): # 可用冒号指明该参数的类型，但调用传参可以不是指定的类型
    ''' 
    画一条线 
    width: 宽度
    char: 字符
    '''
    print(char * width)

line(5, "-")
line(10, "*")
line(width=15,char="#")
