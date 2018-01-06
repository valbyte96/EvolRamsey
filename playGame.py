'''playGame.py
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

def play():
    n = 12
    g = Graph(n)
    g.prep()
    player1 = Player(0, g) # red
    player2 = Player(1, g) # blue
    player1.setStrats(strats) # set strats
    player2.setStrats(strats)
    player1.setStrat(0) # build
    player2.setStrat(random.randint(0,2)) # random or from zoo of opponents

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
    result = play()
    if result == "red": # evolving red
        score+=1.0
    return score

def mainEvol():
    #TODO
    #genome - create a list of size of the number of 
    t=0


def main0():
    print(play())

main0()
