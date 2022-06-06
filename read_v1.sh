#!/bin/bash
read -p "请输入用户名：" user
#-s参数可以使得输入的密码不在终端显示出来，更加安全
read -s -p  "请输入密码：" password
#加双引号可以防止输入的字符中有特殊符号或空格
if [ ! -z "$user" ];then
	useradd "$user"
fi
if [ ! -z "$password" ]
	then
	#用于修改用户密码
	echo "$password" | passwd --stdin $user
fi
#最后这个echo没有输出内容，仅用于脚本执行完换行的作用
#echo
