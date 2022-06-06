#!/bin/bash
function sum()
{

	s=0
	s=`expr $1 + $2`
	echo $s


}
read -p "input your first number: " m
read -p "input your second number: " n
sum $m $n
