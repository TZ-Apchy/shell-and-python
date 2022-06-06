#!/bin/bash
for((i=1;i<=6;i++))
do
   for((j=1;j<=i;j++))
   do
     echo -en "\033[41m  \033[0m"
   done
   echo
done
