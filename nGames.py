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
chrome = ['build','block', 'adv-build', 'adv-block', 'random']
p2Chrome = Chromosome(['build','block', 'adv-build', 'adv-block', 'random'],intervals).getStrats() # all possible chromosomes

# incase fixed
fixed = True
g = Graph(n)
g.setInterval(intervals)
g.prep() # reset graph and prep triangles

'''----------------------------------EVOLUTION----------------------------------------'''



def play(chromosome):
    '''this play function randomizes the graph every game'''
    if fixed:
        g.resetFixed()
    else:
        g.prep() # reset graph and prep triangles
    player1 = Player(0, g) # red
    player2 = Player(1, g) # blue
    
    player1.setStrats(chromosome) # set strat list as well as initial strategy
    #player1.setStrats(p2Chrome[random.randint(0,len(p2Chrome)-1)])
    #player2.setStrats(p2Chrome[random.randint(0,len(p2Chrome)-1)])
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
    '''Every game played on a new random graph on n nodes'''
    nGames = 20 # number of games to play
    p1Wins = 0
    p2Wins = 0
    ties = 0
    chromosome = [3, 3, 3, 3, 3]
    strats = []
    for c in chromosome:
        strats.append(chrome[c])

    for i in range(20):
        win = play(strats)
        if win == "red":
            p1Wins+=1
        elif win == "blue":
            p2Wins+=1
        else:
            ties+=1
    output(p1Wins, p2Wins, ties, nGames)


def output(p1Wins, p2Wins, ties, nGames):
    '''Out puts information about the games played'''
    print("player 1")
    print("total wins:", p1Wins)
    print("win percent:", p1Wins/nGames*100)
    print()
    print("player 2")
    print("total wins:", p2Wins)
    print("win percent:", p2Wins/nGames*100)
    print()
    print("ties:",ties)
    print("win percent:", ties/nGames*100)
    

main()
