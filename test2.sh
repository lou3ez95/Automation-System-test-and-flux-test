#!/bin/bash
# Basic System Info
OS=`head -1 /etc/redhat-release`
HOSTNAME=`uname -n`
INTERFACES=`ip a |cut -d " " -f 2 | sed '/^$/d' | sed 's/://g'|tr '\n' ','`
# System Load
MEM_USED=`free -t -m | grep Total | awk '{print $3" MB";}'`
MEM_TOTAL=`free -t -g | grep "Mem" | awk '{print $2}'`
SWAP_USED=`free -m | tail -n 1 | awk '{print $3}'`
SWAP_TOTAL=`free -g | tail -n 1 | awk '{print $2}'`
CPU=`less /proc/cpuinfo | grep "cpu cores" | cut -d : -f2|cut -d " " -f 2| sed -n '1p'`
CPU_model=`less /proc/cpuinfo | grep "model name" | cut -d : -f2| sed -n '1p'`
MOUNTPOINT=`df -HT | cut -d "%" -f 2 | sed 1d|tr '\n' ','`
date=`date`
#numbers 
mountnbr=`df -hT | cut -d "%" -f 2 | sed 1d|wc -l`
id=`echo $RANDOM`
printf "{\"_id\":\"$id\",\
\"Operating System\":\"$OS\",\
\"Hostname\":\"$HOSTNAME\",\
\"CPU\":{ \
\"CPU_model\":\"$CPU_model\",\
\"CPU_CORES\":\"$CPU\"},\
\"Memory\":\"$MEM_TOTAL\",\
\"Swap\":\"$SWAP_TOTAL\",\
\"Interfaces\":[" > /tmp/result.json


for (( c=1; c <= 4; c++ ))
do
 name=`cat /etc/sysconfig/network-scripts/ifcfg-eth$c | grep "NAME"|cut -d "=" -f 2`
 address=`cat /etc/sysconfig/network-scripts/ifcfg-eth$c | grep "IPADDR"|cut -d "=" -f 2`
 subnet=`cat /etc/sysconfig/network-scripts/ifcfg-eth$c | grep "NETMASK"|cut -d "=" -f 2`
 printf "{\"Name\":\"$name\",\
\"Address\":\"$address\",\
\"Subnet\":\"$subnet\"}" >> /tmp/result.json
 if [ $c != 4 ]
 then
   printf "," >> /tmp/result.json
 fi
 if [ $c == 4 ]
 then
   printf "]," >> /tmp/result.json
 fi

done

printf "\"MountPoint\":[" >> /tmp/result.json

for (( c=1; c <= $mountnbr; c++ ))
do
 mountpoint=`df -HT | cut -d "%" -f 2 | sed 1d|cut -d " " -f 2|sed -n ''$c'p'`
 sysfichier=`df -HT | cut -d " " -f 1 | sed 1d|sed -n ''$c'p'`
 type=`df -HT | awk '{print($2)}' | sed 1d|sed -n ''$c'p'`
 taillemount=`df -HT | sed 1d |  awk '{print $3}'|sed -n ''$c'p'|sed '$!d;s/.$//'|tr "." ","`
 gega=`df -HT | sed 1d |  awk '{print $3}'|sed -n ''$c'p'|grep G`
 first=`echo "1024 $((taillemount))" | awk '{ printf "%f", $1/$2 }'`
 final=`echo "1.024 $first" | awk '{ printf "%.3f", $1/$2 }'`

 if [ -n "$gega" ]
 then
        printf "{\"File_System\":\"$sysfichier\",\
           \"Mount_Point\":\"$mountpoint\",\
           \"Type\":\"$type\",\
	   \"taille\":\"$((taillemount))\"}" >> /tmp/result.json
 else
        printf "{\"File_System\":\"$sysfichier\",\
           \"Mount_Point\":\"$mountpoint\",\
	   \"Type\":\"$type\",\
           \"taille\":\"$final\"}" >> /tmp/result.json
 fi

 if [ $c != $mountnbr ]
 then
   printf "," >> /tmp/result.json
 fi
 if [ $c == $mountnbr ]
 then
   printf "]," >> /tmp/result.json
 fi

done
   printf "\"Date\":\"$date\"}\n" >> /tmp/result.json

