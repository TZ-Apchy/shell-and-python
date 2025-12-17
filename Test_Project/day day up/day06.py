# 问题背景：打印日历
# y:年 m:月 d:日 注：把1、2月当作上一年的13、14月
# 星期几的计算公式：w=(d+2*m+3*(m+1)//5+y+y//4-y//100+y//400)%7+1

def calc_week(y,m,d):
    """根据年月日计算星期几"""
    if m==1 or m==2:
        y-=1
        m+=12
    w=(d+2*m+3*(m+1)//5+y+y//4-y//100+y//400)%7+1
    return w

def is_leap_year(y):
    """判断是否为闰年"""
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        return True
    return False

def calc_day(y,m):
    """计算当月的天数"""
    if m in [1,3,5,7,8,10,12]:
        return 31
    elif m in [4,6,9,11]:
        return 30
    else:
        return 29 if is_leap_year(y) else 28
year=int(input("请输入年份："))
mouth=int(input("请输入月份："))
# year,mouth,day=2010,3,1
# week=calc_week(year,mouth,day)
# print(week)
# print(calc_day(year,mouth))
# year,mouth=2010,2
day=calc_day(year,mouth)
print("一 二 三 四 五 六 日")
print("-"*20)
for i in range(1,day+1):
    w = calc_week(year,mouth,i)
    if i == 1:
        print(f"{' '*(w-1)*3}",end="")   
    elif w == 1:
        print("")
    print(f"{i:2d}",end=" ")

