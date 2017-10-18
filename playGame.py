'''playGame.py
This file ensures that game playing is working properly

'''
from __future__ import absolute_import, division, print_function
import sys, os
from Graph import *
from IterRamsey import *
import random as rand
sys.path.append(os.path.abspath('../pyevolve'))
from pyevolve import *



def play():
    n = 5
    g = Graph(n)
    g.randomize()
    g.countT()
    #g.printGraph()
    player1 = IterRamsey(0, g)
    player2 = IterRamsey(1, g)
    
    while(True):
        if g.done():
            # TODO: win detection
            print("game over")
            break
        player1.play()
        player2.play()

        
        
    print(g.winner(), "wins")
play()
