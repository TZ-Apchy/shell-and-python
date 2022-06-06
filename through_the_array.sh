#!/bin/bash
a=(11 22 33)
#可以用${a[@]}或者${a[*]}来依次遍历数组中的每个元素
for i in ${a[@]}
#for i in ${a[*]}
do
   echo "$i"
done
