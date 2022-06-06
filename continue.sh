#!/bin/bash
for i in {1..5}
#当i取到3时，执行continue，会结束掉当次循环，继续下一次循环，此时脚本并不会退出，最后的echo语句会被执行
do
   [ $i -eq 3 ] && continue
   echo "$i"
done
echo "over"
