nbr=`cat hosts |sed '1,7d'|wc -l`
user=`cat hosts | egrep "ansible_user" |cut -d "=" -f 2`
pass=`cat hosts | egrep "ansible_ssh_pass" |cut -d "=" -f 2`
for (( c=1; c <= $nbr ; c++ ))
do
        add=`cat hosts |sed '1,7d'|sed -n ''$c'p'`
	sshpass -p $pass ssh-copy-id $user@$add -o StrictHostKeyChecking=no > /dev/null 2>&1
done 
