'''evolGame.py
This file ensures that game playing is working properly

'''
from __future__ import absolute_import, division, print_function
import sys, os
from Graph import *
from Player import *
import random as rand
sys.path.append(os.path.abspath('../pyevolve'))
from pyevolve import *

strats0 = ["build", "block", "random"] # change
strats = [["build","build"],["build","block"],["block","build"],["build","random"],["random","build"]
          ,["block","random"],["random","block"],["random","random"],["block","block"]]

'''Here we are evolving player 1'''
def play(strat):
    n = 6
    g = Graph(n)
    g.prep()
    player1 = Player(0, g) # red
    player2 = Player(1, g) # blue
    player1.setStrat(strat[0]) #get starting strategy
    p2Strats = strats[random.randint(0,len(strats)-1)]
    player2.setStrat(p2Strats[0])
    r = 0 # debug
    while(True):
        if g.done(): # stop
            break
        player1.play()
        if g.getPercent()>=.5:
            player1.setStrat(strat[1])
            player2.setStrat(strat[1])
            
        if g.done(): # stop
            break
        if g.getPercent()>=.5:
            player1.setStrat(strat[1])
            player2.setStrat(strat[1])
        player2.play()
        r+=1 # debug

    return g.winner()

def fitness(chromosome):
    score = 0.0
    # plays game once; trying to evolve player 1 
    result = play(chromosome)
    if result == "red": # evolving red
        score+=1.0
    return score

def evalFunc(chromosome):
    score = 0.0
    for c in chromosome:
        result = play(strats[c])
        if result == "red":
            score+=1.0
    return score


def mainEvol():
    genome = G1DList.G1DList(3)
    genome.evaluator.set(evalFunc) #pass in fitness function
    genome.setParams(rangemin=0, rangemax=8)
    ga = GSimpleGA.GSimpleGA(genome)
    ga.setGenerations(20)
    ga.evolve(freq_stats=10)
    print(ga.bestIndividual())

mainEvol()

