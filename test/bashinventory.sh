#!/bin/bash 

#If result.txt is not empty, clean it#
result="result.txt"
if (test -s $result)
  then 
    > $result
fi

###Find IP Address and stock it into a variable###
ip=$(nmap -sP 192.168.6.0/24 |grep "192.168.6." |awk '{print $NF}' |sed 's/(//g' |sed 's/)//g')

echo $ip

###Find MAC Address using result of the variable ip###
#For each value in ip, search and stock the mac address#
for param in $ip
  do
    echo "Traitement de $ip"
    #search MAC Address and result only it#
    mac=$(sudo arping -c 1 $param |grep "bytes" |awk '{print $4}' |head -n 1)
    vendor=$(curl -s "http://www.macvendorlookup.com/api/v2/{$mac}" |jq '.[].company')
    #Stock this result on a list
    list=($param,$mac,$vendor)
    
    echo ${list[*]} >> $result
  done


### Use MAC Address to ask API Rest informations ###
#"""utiliser la variable mac qui se trouve dans for soit utiliser le resultat de la première colonne de result.txt"""

