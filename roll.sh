#!/bin/bash
nane_file="name.txt"
line_file=$(sed -n '$=' $nane_file)
while :
do
  clear
  tmp=$(sed -n "$[RANDOM%line_file+1]p" $nane_file)
  echo -e "\e[32m     随机点名器(按Ctrl+C停止): \e[0m"
  echo -e "\e[32m###############################\e[0m"
  echo -e "\e[32m#                             #\e[0m"
  echo -e "\e[33m          $tmp                 \e[0m"
  echo -e "\e[32m#                             #\e[0m"
  echo -e "\e[32m###############################\e[0m"
  sleep 1
done
