#!/bin/bash
file=`find /root/InputFiles -name "*.csv" | tail -n 1 | cut -d "/" -f 4`
nbr=`cat /root/InputFiles/$file | sed 1d | wc -l `
user=`cat /root/InputFiles/$file | sed 1d | cut -d ";" -f 2 |sed -n '1p'`
password=`cat /root/InputFiles/$file | sed 1d | cut -d ";" -f 3 |sed -n '1p'`
rootpass=`cat /root/InputFiles/$file | sed 1d | cut -d ";" -f 4 |sed -n '1p'`
printf "[all:vars]\n" > /home/ansibleM/tachetelnet/AnsibleProject/hosts
printf "ansible_connection=ssh \n" >> /home/ansibleM/tachetelnet/AnsibleProject/hosts
printf "ansible_user=$user \n" >> /home/ansibleM/tachetelnet/AnsibleProject/hosts
printf "ansible_ssh_pass=$password \n" >> /home/ansibleM/tachetelnet/AnsibleProject/hosts
printf "ansible_become_pass=$rootpass" >> /home/ansibleM/tachetelnet/AnsibleProject/hosts
printf "\n" >> /home/ansibleM/tachetelnet/AnsibleProject/hosts
printf "\n" >> /home/ansibleM/tachetelnet/AnsibleProject/hosts

printf "[servers]\n" >> /home/ansibleM/tachetelnet/AnsibleProject/hosts

for (( c=1; c <= $nbr; c++ ))
do
source=`cat /root/InputFiles/$file | sed 1d | cut -d ";" -f 1|sed -n ''$c'p'`
printf "$source" >> /home/ansibleM/tachetelnet/AnsibleProject/hosts
printf "\n" >> /home/ansibleM/tachetelnet/AnsibleProject/hosts

done

