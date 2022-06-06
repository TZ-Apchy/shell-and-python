#!/bin/bash
date=`date "+%Y-%m-%d"`
if [ ! -f /home/shell_programming/backup/log-$date.tar.gz ];then
	tar -zcPf /home/shell_programming/backup/log-$date.tar.gz /var/log/
fi
