#!/bin/bash 
file=`find /root/uploads -name "*.csv" | tail -n 1 | cut -d "/" -f 4`
nbr=`cat /root/uploads/$file | sed 1d | wc -l `
user=`cat /root/uploads/$file | sed 1d | cut -d ";" -f 2 |sed -n '1p'`
password=`cat /root/uploads/$file | sed 1d | cut -d ";" -f 3 |sed -n '1p'`
rootpass=`cat /root/uploads/$file | sed 1d | cut -d ";" -f 4 |sed -n '1p'`
printf "[all:vars]\n" > /home/ansibleM/tacheOne/hosts
printf "ansible_connection=ssh \n" >> /home/ansibleM/tacheOne/hosts
printf "ansible_user=$user \n" >> /home/ansibleM/tacheOne/hosts
printf "ansible_ssh_pass=$password \n" >> /home/ansibleM/tacheOne/hosts
printf "ansible_become_pass=$rootpass" >> /home/ansibleM/tacheOne/hosts
printf "\n" >> /home/ansibleM/tacheOne/hosts
printf "\n" >> /home/ansibleM/tacheOne/hosts

printf "[servers]\n" >> /home/ansibleM/tacheOne/hosts

for (( c=1; c <= $nbr; c++ ))
do
source=`cat /root/uploads/$file | sed 1d | cut -d ";" -f 1|sed -n ''$c'p'`
printf "$source" >> /home/ansibleM/tacheOne/hosts  
printf "\n" >> /home/ansibleM/tacheOne/hosts

done

