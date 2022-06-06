#!/bin/bash
#for i等价于for i in $@或$*的效果，遍历所有参数
#for i in $@
#for i in $*
for i
do
	let sum+=$i
done
echo "sum的值为：$sum"
