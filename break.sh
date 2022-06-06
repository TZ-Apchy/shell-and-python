#!/bin/bash
for i in {1..5}
#当i取到3时，执行break，会结束循环体，但是不影响循环体外的脚本执行，则最后的echo语句会被执行
do
   [ $i -eq 3 ] && break
   echo "$i"
done
echo "over"
