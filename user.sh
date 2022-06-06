#!/bin/bash
read -p "请输入用户名：" user
if [ -z "$user" ];then
   echo -e "\033[32m未输入用户名，脚本将退出...\033[0m"
   exit
fi
read -p  "请输入密码：" password
#如果不输入密码，密码会默认取123456
password=${password:-123456}
useradd "$user"
echo "$password" | passwd --stdin "$user"
