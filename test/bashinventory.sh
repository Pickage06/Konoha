#!/bin/bash 

#If result.txt is not empty, clean it#
result="result.txt"
if (test -s $result)
  then 
    > $result
fi

###Find IP Address and stock it into a variable###
ip=$(nmap -sP 192.168.6.0/24 |grep "192.168.6." |awk '{print $6}' |sed 's/(//g' |sed 's/)//g')

echo $ip

###Find Mac address using result of the variable before###
#For each value in a, search and stock the mac address#
for param in $ip
  do
    #search mac address and result only it#
    mac=$(sudo arping -c 1 $param |grep "bytes" |awk '{print $4}')
    #Stock this result on a list
    list=($param,$mac)
    
    echo ${list[*]} >> $result
  done
