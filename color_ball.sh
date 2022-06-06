#!/bin/bash
red_ball=""
blue_ball=""
while :
do
   clear
   echo "---机选双色球---"
   tmp=$[$RANDOM%33+1]
   echo "$red_ball" | grep -q -w "$tmp" && continue
   red_ball+="$tmp "
   echo -en "\033[31m$red_ball\033[0m"
   word=$(echo "$red_ball" | wc -w)
   if [ $word -eq 6 ];then
      blue_ball=$[$RANDOM%16+1]
      echo -e "\033[34m$blue_ball\033[0m"
      break
   fi
   sleep 1
done
