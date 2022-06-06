#!/bin/bash
for i in $*
do
	echo "I love $i"
done
for j in $@
do
        echo "I love $j"
done
