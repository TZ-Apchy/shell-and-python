#!/bin/bash
for i in $(ls /etc/*.conf)
do
    md5sum $i >> /home/shell_programming/data.log
done
