#!/bin/bash
if [ -z "$1" ];then
	echo -n "用法：脚本 "
	echo -e "\033[32m域名或IP\033[0m"
	exit
fi
#-c参数设置ping的次数；-i参数设置ping的时间间隔；-W参数设置超时时间；&表示ping的标准输出和错误输出都丢弃不显示在屏幕上
ping -c2 -i0.1 -W1 "$1" &>/dev/null
if [ $? -eq 0 ];then
	echo "$1 is up"
else
	echo "$1 is down"
fi
