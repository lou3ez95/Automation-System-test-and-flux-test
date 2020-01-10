#!/bin/bash
#echo "This script is about to run another first script for hosts concern."
sh /home/ansibleM/tachetelnet/AnsibleProject/Shellhosts.sh
#echo "This script has just run another script."

#echo "This script is about to run another second script for SDP concern."
sh /home/ansibleM/tachetelnet/AnsibleProject/shell.sh
#echo "This script has just run another script."


sh /home/ansibleM/tachetelnet/AnsibleProject/ping.sh
ansible-playbook  /home/ansibleM/tachetelnet/AnsibleProject/MainPlaybook -i  /home/ansibleM/tachetelnet/AnsibleProject/hosts
 
