from __future__ import absolute_import, division, print_function
'''---------------------------------nGames.py----------------------------------------
plays the game n times and records the win percentage 
'''

'''---------------------------------IMPORTS----------------------------------------'''
import sys, os
from Graph import *
from Player import *
from Chromosome import *
import random as rand
sys.path.append(os.path.abspath('../pyevolve'))
from pyevolve import *
'''----------------------------------GLOBALS----------------------------------------'''
intervals = 5 # number of game intervals
n = 7 # number of nodes
chrome = ['build','block','random']
p2Chrome = Chromosome(['build','block','random'],intervals).getStrats() # all possible chromosomes

#g = Graph(n) # global graph
'''----------------------------------EVOLUTION----------------------------------------'''

def playOnFixed():
    print("TODO")

def play(chromosome):

    g = Graph(n)
    g.setInterval(intervals)
    g = Graph(n) 
    g.prep() # reset graph and prep triangles
    player1 = Player(0, g) # red
    player2 = Player(1, g) # blue
    
    player1.setStrats(chromosome) # set strat list as well as initial strategy
    player2.setStrats(p2Chrome[random.randint(0,len(p2Chrome)-1)])
    player2.setStrats(['random', 'random','random','random','random'])
    
    r = 0 # debug
    unit = g.getNumEdges()/intervals

    # randomizes who goes first
    first = rand.randint(0,1)
    
    
    while(True):
        if first==0: # player 1 goes first
            if g.done(): # stop
                break
            player1.play()
            g.checkInterval(player1, player2)
                
            if g.done(): # stop
                break

            player2.play()
            g.checkInterval(player1, player2)
            r+=1 # debug

        else: # player 2 goes first
            if g.done(): # stop
                break
            player2.play()
            g.checkInterval(player1, player2)
                
            if g.done(): # stop
                break

            player1.play()
            g.checkInterval(player1, player2)
            r+=1 # debug

    return g.winner()

    


def main():
    n = 20 # number of games to play
    p1Wins = 0
    p2Wins = 0
    chromosome = [0, 0, 0, 0, 0]
    strats = []
    for c in chromosome:
        strats.append(chrome[c])

    for i in range(20):
        win = play(strats)
        if win == "red":
            p1Wins+=1
        else:
            p2Wins+=1
    print("player 1")
    print("total wins:", p1Wins)
    print("win percent:", p1Wins/n)
    print()
    print("player 2")
    print("total wins:", p2Wins)
    print("win percent:", p2Wins/n)



main()
