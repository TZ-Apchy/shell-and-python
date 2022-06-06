#!/bin/bash
if rpm -q vsftpd &>/dev/null;then
	echo "vsftp已安装"
else
	yum -y install vsftpd
fi
systemctl restart vsftpd
