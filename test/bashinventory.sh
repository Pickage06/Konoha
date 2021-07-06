#!/bin/bash 


###Find IP Address###
a=$(nmap -sP 192.168.6.0/24 |grep "192.168.6." |awk '{print $6}' |sed 's/(//g' |sed 's/)//g')

echo $a 

###Find Mac address###
for param in $a
  do
    param=sudo arping -c 1 $a 
    echo $param
  done
#mac=$(sudo arping -c 1 192.168.6.2)
#echo $mac
