from __future__ import absolute_import, division, print_function
'''---------------------------------evolGame2.py----------------------------------------
evolution happens here
Different approach to evolution that evolGame.py
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
n = 10 # number of nodes

# incase fixed
fixed = True
g = Graph(n)
g.setInterval(intervals)
g.prep() # reset graph and prep triangles

chrome = ['build','block','random']
p2Chrome = Chromosome(['build','block','random'],intervals).getStrats() # all possible chromosomes

#g = Graph(n) # global graph
'''----------------------------------EVOLUTION----------------------------------------'''

'''Evolution for player 1: 'red' '''
def play(chromosome):
    strats = []
    for c in chromosome:
        strats.append(chrome[c])
    if fixed:
        g.resetFixed()
    else:
        g.prep() # reset graph and prep triangles
    player1 = Player(0, g) # red
    player2 = Player(1, g) # blue
    
    player1.setStrats(strats) # set strat list as well as initial strategy
    player2.setStrats(p2Chrome[random.randint(0,len(p2Chrome)-1)])
    #player2.setStrats(['build','build', 'build', 'build', 'build'])
    #player2.setStrats(['block','block', 'block', 'block', 'block'])
    #player2.setStrats(['random','random', 'random', 'random', 'random'])
    
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

    
def evalFunc(chromosome):
    score = 0.0
    result = play(chromosome)
    if result == "red":
        score+=1.0
    return score


def testMain():
    print(play([2,2,2,2]))


def mainEvol():
    genome = G1DList.G1DList(intervals) # create random list of numbers
    genome.evaluator.set(evalFunc) #pass in fitness function
    genome.setParams(rangemin=0, rangemax=len(chrome)-1) #set range for numbers
    ga = GSimpleGA.GSimpleGA(genome)
    ga.setGenerations(10)
    ga.evolve(freq_stats=5)
    print(ga.bestIndividual())

mainEvol()
#testMain()
