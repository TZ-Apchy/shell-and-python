#!/bin/bash
clear
#RANDOM是系统自带的取随机数的变量，如：echo "$RANDOM"会生出一个随机数，这里取余会生成0-9以内的随机数，运算加上1则为1-10以内的随机数
num=$[RANDOM%10+1]
read -p "请输入1-10之间的整数：" guess
if [ $guess -eq $num ];then
	echo "恭喜，猜对了，就是：$num"
elif [ $guess -lt $num ];then
	echo "猜小了"
else
	echo "猜大了"
fi