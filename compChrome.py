from __future__ import absolute_import, division, print_function
'''---------------------------------nGames.py----------------------------------------
plays the game n times and records the win percentage for on a list of chromosomes
'''
import matplotlib.pyplot as plt
import numpy as np
'''---------------------------------IMPORTS----------------------------------------'''
import sys, os
from Graph import *
from Player import *
from Chromosome import *
import random as rand
sys.path.append(os.path.abspath('../pyevolve'))
from pyevolve import *
import cPickle as pickle
'''----------------------------------GLOBALS----------------------------------------'''
intervals = 5 # number of game intervals
n = 15 # number of nodes
chrome = ['build','block', 'adv-build', 'adv-block', 'random']
p2Chrome = Chromosome(['build','block', 'adv-build', 'adv-block', 'random'],intervals).getStrats() # all possible chromosomes

# IF YOU WANT PICKLED FIXED GRAPHS
filehandler = open('GraphList_n15_L3.obj', 'r') 
graphList = pickle.load(filehandler) # list of random graph objects
# incase fixed
fixed = True
#g = Graph(n)
g = graphList[0]
g.setInterval(intervals)
g.prep() # reset graph and prep triangles

'''----------------------------------PLAY----------------------------------------'''



def play(chromosome):
    '''this play function randomizes the graph every game'''
    
    if fixed:
        g.resetFixed()
    else:
        g.prep() # reset graph and prep triangles
    player1 = Player(0, g) # red
    player2 = Player(1, g) # blue
    
    player1.setStrats(chromosome) # set strat list as well as initial strategy
    player2.setStrats(p2Chrome[random.randint(0,len(p2Chrome)-1)])
    
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

    


def playN(chromosome):
    '''Play game n times in order to compare strategies'''
    nGames = 1000 # number of games to play
    p1Wins = 0
    p2Wins = 0
    ties = 0
    strats = []
    for c in chromosome:
        strats.append(chrome[int(c)])

    for i in range(nGames):
        win = play(strats)
        if win == "red":
            p1Wins+=1
        elif win == "blue":
            p2Wins+=1
        else:
            ties+=1
    return [p1Wins, p2Wins, ties]


def main():
    result = []
    #C = [['1', '4', 4, 0, 3],[0, 0, 3, 2, 0],[0, 0, 3, 2, 0]]
    C = input("input results: ")
    for c in C:
        result.append(playN(c))
    graph(result)

def graph(sample):
    #sample = [[69, 175, 6], [148, 90, 12], [154, 83, 13]]

    objects = ["G"+str(i) for i in range(len(sample))]
    wins = [L[0] for L in sample] # list of wins
    losses =  [L[1] for L in sample]
    ties =  [L[2] for L in sample]

    # chart portion
    fig, ax = plt.subplots()
    ind = np.arange(len(objects))
    width = 0.25
    rects1 = ax.bar(ind, wins, width, color='g')
    rects2 = ax.bar(ind + width, losses, width, color='r')
    rects3 = ax.bar(ind + 2*width, ties, width, color='y')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(objects)
    

    plt.show()

    

        


    

main()
