#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nmap3
#pip3 install python-nmap
import os 
######## INVENTORY HARDWARE ########
"""The objective of the script is to make an inventory
 of all the equipments on a factory. To do that, please observe 
 the following instructions  """


######TODO######
#If result.txt is not empty, clean it#
def empty_file():
  empty_file = os.stat("result.txt").st_size == 0
  if empty_file == False:
    open("result.txt", "w").close()

###Find IP Address###
#Do a nmap in your subnet#
nm = nmap3.Nmap()
result = nm.nmap_subnet_scan("192.168.6.0/24")

#For all key in the dico, show them#
#for key in result.keys():
#  print(key)

#Extract the IPs address of the nmap and Stock it into a list#
#Extract keys associated to ip address#
ips=list(result.keys())[:1] 
#print(ip) >> result.txt
print(*ips, sep = ',')

###Find MAC Address###
def arping():
  for ip in ips():
    arpreq.arpreq(ip)

print(arping)
##Ping address##"+ list of only IP Address"
##Stock all informations##
"{dict}" "+ list of only IP Address"
###Find API Constructor###
"""With @MAC ask to the api constructor informations"""
###Stock informations on a table {dict}###
"""Create dictionnary to stock informations"""
###Inform script's user to the result###
"""Tell to the user what it was find or not but show informations like
 the IP Address"""
