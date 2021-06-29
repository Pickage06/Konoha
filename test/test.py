#!/usr/bin/env python3

##Test training: it's a vote##
##TODO#
#Create a list of candidates#
#Create a list of mentions for votes#
#Create random votes
#Choose a random Candidate
#Create a table to insert candidates and theirs mentions# 


##Setup votes##
#Declaration of candidates' list (dictionnary)#
Candidates = {
  "Hermione":"Hermione Granger",
  "Hulk":"Bruce Baner",
  "Spiderman": "peter Parker",
  "Walter": "Walter white",
  "Vador": "Anakine Skywalker",
  "Fiona": "princesse fiona"
}

#Declaration of the mention's list(list)#
Mentions = [
  "Excellent",
  "Great",
  "Good", 
  "Just",
  "Not intersting",
]


##Fonctions##

import random

#Create random vote#
def rand_votes(vote):
  my_rand = random.randint(0,4)
  result = vote[my_rand]
  return result

#Choose a random candidate#
def rand_cand(candidate):
  my_rand2 = random.randint(0,5)
  maj = candidate[my_rand2].capitalize()  
  return maj


print(rand_cand(Candidates))
print(rand_votes(Mentions))
#Create a table for subscribe all of votes(dictionnary)#
#def table():
  #votes.  
  
