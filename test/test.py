#!/usr/bin/env python3

import random

##Test training: it's a vote##
##TODO#
#Create a list of candidates#
#Create a list of mentions for votes#
#Create random votes
#Choose a random Candidate
#Create a table to insert candidates and theirs mentions# 

##Setup votes##
#Declaration of numbers'votes
VOTES = 10000

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

#Create random vote#
def rand_votes(vote):
  my_rand = random.randint(0,4)
  result = vote[my_rand]
  return result  
#Choose a random candidate#
def rand_cand(candidate):
  my_rand2 = random.choice(list(Candidates.values()))
  return candidate[my_rand2]  
  
#Nom = rand_cand(Candidates).values
#print(Nom)
print(rand_votes(Mentions))
print(rand_cand(Candidates))

#Create a table for subscribe all of votes(dictionnary)#
#def table():
  #votes.  
  
