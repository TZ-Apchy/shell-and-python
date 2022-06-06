#!/bin/bash
until [ $# -eq 0 ]
do
	userdel -r $1
	echo "$1 is delted"
	shift
done
