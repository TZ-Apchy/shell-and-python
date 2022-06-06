#!/bin/bash
read -p "Are you sure?(y/n):" sure
case $sure in
#|表示或者关系，后面双分号可以写在下一行，也可以写在同一行，表示结束，若有多条语句，只用在最后一条语句加双分号即可
y|Y|yes|YES)
	echo "you enter $sure,OK";;
n|N|no|NO)
	echo "you enter $sure,OVER"
	;;
*)
#最后一条语句的结束符;;可以省略
	echo "error"
esac
