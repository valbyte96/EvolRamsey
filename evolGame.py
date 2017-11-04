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

strats = ["build", "block", "random"]

'''Here we are evolving player 1'''
def play():
    n = 12
    g = Graph(n)
    g.prep()
 #  g.printGraph()
    player1 = Player(0, g) # red
    player2 = Player(1, g) # blue
    player1.setStrat("build")
    player2.setStrat("build")
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

        
   # print("rounds",r) # Debugger
   # TODO rounds bug
   # print("game over")
   # print(g.winner(), "wins")
   return g.winner()

def fitness(chromosome):
    score = 0.0
    # plays game once; trying to evolve player 1 
    result = play()
    if result == "red": # evolving red
        score+=1.0
    return score


def mainEvol():
    #TODO
    #genome - create a list of size of the number of
    
    # tell Python what fitness function is 
    genome.evaluator.set(fitness) #pass in fitness function

    # create genetic algorithm enguine 
    ga = GSimpleGA.GSimpleGA(genome)

    # run the evolutionary process
    ga.evolve(freq_stats=10) #runs ge; reports every 10 gens

