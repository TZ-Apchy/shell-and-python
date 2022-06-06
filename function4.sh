#!/bin/bash
#可以直接通过函数名来定义函数
function add {
  echo "$[$1+$2]"
} 
add 1 2
add 8 10 
