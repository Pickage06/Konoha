#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import random
 
##Test training: it's a vote##
##TODO#
#Create a list of candidates#
#Create a list of mentions for votes#
#Create random votes
#Choose a random Candidate
#Create a table to insert candidates and theirs mentions# 
#random.seed(0)

##Create number votes##
VOTES = 10000

##create a dictionnary for candidates##
Candidates = {
  "hermione": "Hermione GRANGER",
  "balou": "Balou l'ours",
  "Spiderman": "Peter PARKER",
  "gandalf": "Gandalf the white",
  "Walter" : "walter White"
}

##Create a list for mentions##
Mentions = [
  "Excelent", 
  "Very good",
  "good",
  "Bof",
  "passable",
  "Not Possible"
]

####Fonctions####

##Create a random vote##
def rand_vote(vote):
  my_rand = random.randint(0,5)
  result = vote[my_rand].capitalize()
  return result


##Choose a random candidate
def rand_cand(cand):
  my_rand2 = random.choice(list(Candidates.keys()))
  cand = my_rand2.capitalize()
  return cand

##Add their randoms to the table##
def add_vote(table):
  for _ in range(0,VOTES):
  mention = (rand_vote(Mentions))
  candidate = (rand_cand(Candidates))

