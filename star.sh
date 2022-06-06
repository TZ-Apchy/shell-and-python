#!/bin/bash
#没有循环嵌套，打印一排5个*
for i in {1..5}
do
   echo -n "* "
done
echo
echo

#有循环嵌套，打印5排，每排5个*
for i in {1..5}
do
   for j in {1..5}
   do
     echo -n "* "
   done
   echo
done
