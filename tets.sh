#!/bin/bash

mountnbr=`df -hT | cut -d "%" -f 2 | sed 1d|wc -l`
for (( c=1; c <= $mountnbr; c++ ))
do
 mountpoint=`df -HT | cut -d "%" -f 2 | sed 1d|cut -d " " -f 2|sed -n ''$c'p'`
 sysfichier=`df -HT | cut -d " " -f 1 | sed 1d|sed -n ''$c'p'`
 taillemount=`df -HT | sed 1d |  awk '{print $3}'|sed -n ''$c'p'|sed '$!d;s/.$//'`
 gega=`df -HT | sed 1d |  awk '{print $3}'|sed -n ''$c'p'|grep G`
 final1=`echo "1024 $((taillemount))" | awk '{ printf "%f", $1/$2 }'`
 final=`echo "1.024 $final1" | awk '{ printf "%.3f", $1/$2 }'`
 printf "{\"File System\":\"$sysfichier\",\
	   \"Mount Point\":\"$mountpoint\",\""

 if [ -n "$gega" ]
 then
	printf "{\"taille\":\"$((taillemount*2))\"}"
 else 
 	printf "{\"taille\":\"$final\"}"
 fi

done
