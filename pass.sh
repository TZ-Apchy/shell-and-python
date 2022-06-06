#!/bin/bash
#指定随机字符串，生成10位的随机密码
key="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
pass=""
for i in {1..10}
do
   num=$[RANDOM%${#key}]
   tmp=${key:num:1}
   pass=${pass}${tmp}
done
echo $pass
