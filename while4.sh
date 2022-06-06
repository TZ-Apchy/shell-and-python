#!/bin/bash
PREFIX="test";i=1
while [ $i -le 5 ]
do
     useradd ${PREFIX}$i
     echo "123456" | passwd --stdin ${PREFIX}$i &>/dev/null
     let i++

done
