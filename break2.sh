#!/bin/bash
for i in {1..7}
#当j取到2时，执行到break时，只会结束j所在的循环体，但是不影响循环体外的循环体以及脚本的执行，即i的值还会按需输出且最后的echo语句也会被执行
do
   echo "$i"
   for j in {1..3}
   do
	if [ $j == 2 ];then
		echo "j is $j"
		break
	fi	
   done
done
echo "over"
