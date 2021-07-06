#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nmap

######## INVENTORY HARDWARE ########
"""The objective of the script is to make an inventory
 of all the equipments on a factory. To do that, please observe 
 the following instructions  """


######TODO######
###Find IP Address###
ip = nmap -sP 192.168.6.0/24 |grep "192.168.6." |awk '{print $6}' |sed 's/(//g' |sed 's/)//g'
print(ip)
###Find MAC Address###
"""With NMAP or PING + ARP or AWK"""

##Ping address##"+ list of only IP Address"
##Extract MAC address##
##Stock all informations##
"{dict}" "+ list of only IP Address"
###Find API Constructor###
"""With @MAC ask to the api constructor informations"""
###Stock informations on a table {dict}###
"""Create dictionnary to stock informations"""
###Inform script's user to the result###
"""Tell to the user what it was find or not but show informations like
 the IP Address"""
