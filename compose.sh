#!/bin/bash
#多个数排列组合
for i in {1..3}
do
   for j in {1..3}
   do
     for k in {1..3}
     do
        echo "$i$j$k"
#        echo "${i}${j}${k}"
     done
   done
done
