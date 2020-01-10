#!/bin/bash

#counting the number of lines in converted hosts file, eliminate the first line,
nbr1=`cat /home/ansibleM/tachetelnet/AnsibleProject/hosts | sed 1d | wc -l`
file=`find /root/InputFiles2 -name "*.csv" | tail -n 1 | cut -d "/" -f 4`
for (( c=1; c <= $nbr1; c++ )) 
do

#taking the first elements which is the source address in each line of the file
sources=`cat /home/ansibleM/tachetelnet/AnsibleProject/hosts | sed 1d | cut -d " " -f 1 | sed -n ''$c'p'`

#showing the lines of the hosts converted file for each source address
nbr2=`cat /root/InputFiles2/$file | sed 1d | egrep "^$sources" | wc -l`

printf "IPVARS:\n" > /home/ansibleM/tachetelnet/AnsibleProject/$sources

     for (( i=1; i <= $nbr2; i++ ))
     do

        dests=`cat /root/InputFiles2/$file | sed 1d | egrep "^$sources" | cut -d ";" -f 2 | sed -n ''$i'p'` 
        ports=`cat /root/InputFiles2/$file | sed 1d | egrep "^$sources" | cut -d ";" -f 3 | sed -n ''$i'p'`

        printf "  - IPname: $dests\n" >> /home/ansibleM/tachetelnet/AnsibleProject/$sources
        printf "    Port:\n" >> /home/ansibleM/tachetelnet/AnsibleProject/$sources 
        printf "      - Port_nb: $ports\n" >> /home/ansibleM/tachetelnet/AnsibleProject/$sources

     done 
done





