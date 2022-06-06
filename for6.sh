#!/bin/bash
#{1..10}表示取1~10之间的数字，如echo {a..z}
for i in {1..10}
do
  	useradd test$i
	echo "123456" | passwd --stdin test$i
done
