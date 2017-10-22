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



def play():
    n = 12
    g = Graph(n)
    g.randomize()
    g.countT()
 #  g.printGraph()
    player1 = Player(0, g) # red
    player2 = Player(1, g) # blue
    r = 0
    while(True):
        if g.done():
            # TODO: win detection
            print("game over")
            break
        player1.play()
        player2.play()
        r+=1

        
   # print("rounds",r) # Debugger
   # TODO rounds bug
    print(g.winner(), "wins")
play()
