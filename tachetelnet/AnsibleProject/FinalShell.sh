#!/bin/bash

ligne=`python filter.py $2 | sed 's/["{]//g' |sed "s/['}]//g" | sed 's/[][]//g' | sed "s/[()]//g" | wc -l`
id=`echo $RANDOM`
#priting a symbol for json, the $ means it takes the first parameter after calling the script

printf "{\"_id\":\"$id\",\
         \"Source\":\"$1\",\
         \"Destination\":[ " > /tmp/results/$1.json

for (( c=1; c <= $ligne; c++ ))
#here we are going the take each part of the lines so we can print it later
do
  IPNAME=`python filter.py $2|sed -n ''$c'p'| sed 's/["{]//g' |sed "s/['}]//g" | sed 's/[][]//g' | sed "s/[()]//g" |cut -d "," -f 1 | cut -d ":" -f 2 | sed 's/[u]//g'|cut -d " " -f 2`
  PORT=`python filter.py $2|sed -n ''$c'p'| sed 's/["{]//g' |sed "s/['}]//g" | sed 's/[][]//g' | sed "s/[()]//g" |cut -d "," -f 2 | cut -d ":" -f 2 `
  STATUS=`python filter.py $2|sed -n ''$c'p'| sed 's/["{]//g' |sed "s/['}]//g" | sed 's/[][]//g' | sed "s/[()]//g" |cut -d "," -f 3 | cut -d ":" -f 3`
  Date=`python filter.py $2|sed -n ''$c'p'| sed 's/["{]//g' |sed "s/['}]//g" | sed 's/[][]//g' | sed "s/[()]//g" |cut -d "," -f 4 | cut -d "." -f 1 | sed 's/[u]//g' | cut -d " " -f 2,3`
       
 printf "{\"Ip\":\"$IPNAME\",\
          \"PORT\":\"$PORT\",\
          \"details\":\"$STATUS\",\
          \"Started\":\"$Date\"}"  >> /tmp/results/$1.json
#add a , in lines before the ending line, because the last line with , present an error, so if we didnt reach the end of file it will add a ,
  if [ $c != $ligne ]
  then
       printf "," >> /tmp/results/$1.json
  fi
  if [ $c == $ligne ]
  then
       printf "]" >> /tmp/results/$1.json
  fi

done

printf "}\n" >> /tmp/results/$1.json

