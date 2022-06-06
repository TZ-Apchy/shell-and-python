#!/bin/bash
#获取user.txt中的用户名
for i in `cat user.txt`
do
  	useradd $i
	echo "123456" | passwd --stdin $i
done
