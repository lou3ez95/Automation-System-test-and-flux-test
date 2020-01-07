#!/bin/bash
sh /home/ansibleM/tacheOne/conver.sh > /dev/null 2>&1
sh /home/ansibleM/tacheOne/ping.sh > /dev/null 2>&1
ansible-playbook -i  /home/ansibleM/tacheOne/hosts  /home/ansibleM/tacheOne/config.yml --extra-var patern=$1

