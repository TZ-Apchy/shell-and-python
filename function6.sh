#!/bin/bash
function myping {

   ping -c3 -i0.2 -W1 "$1" &>/dev/null
   if [ $? -eq 0 ];then
	echo "$1 is up"
   else
	echo "$1 is down"
   fi
}
for i in {1..254}
do
   myping "121.4.90.$i" &
done
#此处wait的作用是使所有后台进程全部执行完才退出脚本，不至于处于一种假的卡死状态
wait
