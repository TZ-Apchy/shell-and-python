#!/bin/bash
#{1..10}表示取1~10之间的数字，如echo {a..z}
for i in {1..10}
do
  	userdel -r test$i
	echo "删除用户：test$i成功"
done
