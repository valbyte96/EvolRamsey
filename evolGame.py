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

strats = ["build", "block", "random"] # change

'''Here we are evolving player 1'''
def play(strat):
    n = 5
    g = Graph(n)
    g.prep()
    g.setVerbose(0)
 #  g.printGraph()
    player1 = Player(0, g) # red
    player2 = Player(1, g) # blue
    player1.setStrat(strat) #get random allele
    player2.setStrat(strats[random.randint(0,len(strats)-1)])
    r = 0 # debug
    while(True):
        if g.done(): # stop
            break
        # TODO: set strat
        player1.play()
        if g.done(): # stop
            break
        # TODO: set strat
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
        if c==0:
            result = play("build")
            if result == "red":
                score+=1.0
        elif c==1:
            result = play("block")
            if result == "red":
                score+=1.0
        else:
            result = play("random")
            if result == "red":
                score+=1.0
    return score


def mainEvol():
    genome = G1DList.G1DList(3)
    genome.evaluator.set(evalFunc) #pass in fitness function
    genome.setParams(rangemin=0, rangemax=2)
    ga = GSimpleGA.GSimpleGA(genome)
    ga.setGenerations(20)
    ga.evolve(freq_stats=10)
    print(ga.bestIndividual())

mainEvol()

