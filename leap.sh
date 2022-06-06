#!/bin/bash
for i in {1..5000}
do
	if [[ $[i%4] -eq 0 && $[i%100] -ne 0 || $[i%400] -eq 0 ]];then
		echo "$i:是闰年"
	else
		echo "$i:非闰年"
	fi
done
