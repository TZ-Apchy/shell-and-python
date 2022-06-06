#!/bin/bash
num=10
until [ $num -gt 20 ];do
	echo $num
	num=$((num+1))
done
