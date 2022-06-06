#!/bin/bash
bar() {
while :
#42m后面有个空格，最后会显示成色块
do
   echo -en "\033[42m \033[0m"
   sleep 1
done
}
bar &
cp -r $1 $2
kill $!
echo
