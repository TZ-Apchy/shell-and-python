#!/bin/bash
for i in {1..5}
#当i取到3时，会执行exit结束整个脚本，最后面的echo语句也不会被执行
do
   [ $i -eq 3 ] && exit
   echo "$i"
done
echo "over"
