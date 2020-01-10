#!/bin/bash

#count the number of lines, we take only the first part as the result which is the number of lines, after the space we remove the other part of the result
ligne=`wc -l /tmp/result.txt|cut -d " " -f 1`

# printing a symbol for json, the $ means it takes the first parameter after calling the script
printf "[" > /tmp/results/$1.json


for (( c=1; c <= $ligne; c++ ))

#here we are going the take each part of the lines so we can print it later

do
  IPNAME=`cat /tmp/result.txt| cut -d , -f 1 | cut -d : -f 2|sed 1d`
  PORT=`cat /tmp/result.txt|sed -n ''$c'p'| cut -d , -f 2 | cut -d : -f 2`
  STATUSFAILED=`cat /tmp/result.txt|sed -n ''$c'p'| cut -d , -f 3| sed 's/)//g'`

 printf "{\"@Ip\":\"$IPNAME\",\
\"PORT\":\"$PORT\",\
\"Failed\":\"$STATUSFAILED\"}" >> /tmp/results/$1.json 

#add a , in lines before the ending line, because the last line with , present an error, so if we didnt reach the end of file it will add a ,
  if [ $c != $ligne ]
  then
       printf "," >> /tmp/results/$1.json 
  fi

done

printf "]\n" >> /tmp/results/$1.json

