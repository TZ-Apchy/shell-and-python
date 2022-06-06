#!/bin/bash
#可以直接通过函数名来定义函数
function cecho {
  echo -e "\033[$1m$2\033[0m"
}
cecho 31 OK
cecho 32 OK
cecho 33 Error
