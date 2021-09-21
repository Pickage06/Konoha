#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nmap3
import os 
import pickle
import arpreq
import requests
import json
######## INVENTORY HARDWARE ########
"""The objective of the script is to make an inventory
 of all the equipments on a factory. To do that, please observe 
 the following instructions  """


######TODO######
#If result.txt is not empty, clean it#
def empty_file():
  empty_file = os.stat("result.txt").st_size == 0 #"""check if the file result.txt exist and it size is more than 0"""
  if empty_file == False:
    open("result.txt", "w").close()

###Find IP Address###
#Do a nmap in your subnet#
nm = nmap3.Nmap()
result = nm.nmap_subnet_scan("192.168.6.129/32")

#Extract the IPs address of the nmap and Stock it into a list#
#Extract keys associated to ip address#
ips=list(result.keys())[:-2] #"""without the result stats and runtime""" 
#fileresult = open("result.txt", "w").close() """Open the file result.txt and write the result of ips"""
#print(*ips, sep = ',')
print(ips)

###Find MAC Address###
def arping():
  for ip in ips:
    mac = arpreq.arpreq(ip)
    print(mac)
    #url_api = "http://www.macvendorlookup.com/api/v2/{"+ mac +"}"
    #response_api = requests.get(url_api) 
    #response_json = response_api.json() 
    #print(response_json)

arping()

###Find API Constructor###
"""With @MAC ask to the api constructor's informations"""
def vendor():
    #Transform the url's mac address by the variable mac 
    url_api = "http://www.macvendorlookup.com/api/v2/{"+ mac +"}"
    #Get the response of the api requests through the url
    response_api = requests.get(url_api) 
    #Change the api's result in json format
    response_json = response_api.json() 
    #Display the result
    print(response_json)
    
vendor()

"""Recover information of the company"""
###Stock informations on a table {dict}###
"""Create dictionnary to stock informations"""
###Inform script's user to the result###
"""Tell to the user what it was find or not but show informations like
 the IP Address"""
