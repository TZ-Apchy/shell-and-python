#!/bin/bash
#\e效果和\033一样
clear
echo -e "\033[42m----------\033[0m    "
echo -e "#\e[32m 1.查看网卡信息\e[0m #"
echo -e "#\e[33m 2.查看内存信息\e[0m #"
echo -e "#\e[34m 3.查看磁盘信息\e[0m #"
echo -e "#\e[35m 4.查看CPU信息\e[0m  #"
echo -e "#\e[36m 5.查看账户信息\e[0m #"
echo -e "\033[42m----------\033[0m    "
echo
read -p "请输入选项[1-5]:" key
case $key in
1)
  ifconfig eth0 | grep "inet ";;
2)
  mem=$(free -h | grep "Mem" | tr -s " " | cut -d " " -f 7)
  echo "本机内存剩余容量为：$mem";;
3)
  root_free=$(df -h | grep "/$" | tr -s " " | cut -d " " -f 4)
  echo "本机根分区剩余容量为：$root_free";;
4)
  cpu=$(uptime | tr -s " " | cut -d " " -f 13)
  echo "本机CPU 15分钟的平均负载为：$cpu";;
5)
  login_number=$(who | wc -l)
  total_number=$(cat /etc/passwd | wc -l)
  echo "当前系统账户为：$USER"
  echo "当前系统登录的系统账户数量为：$login_number"
  echo "当前系统中总用户数量为：$total_number";;
*)
  echo "输入有误，超出1-5的范围";;
esac
