from __future__ import absolute_import, division, print_function
'''---------------------------------evolGame4.py----------------------------------------
evolution happens here
Different approach to evolution that evolGame.py
Difference between previous evolGame files is that this utilizes
pickled graph objects

'''

'''---------------------------------IMPORTS----------------------------------------'''
import sys, os
from Graph import *
from Player import *
from Chromosome import *
import random as rand
sys.path.append(os.path.abspath('../pyevolve'))
from pyevolve import *
import cPickle as pickle

'''----------------------------------GAME GLOBALS----------------------------------------'''
intervals = 5 # number of game intervals
chrome = ['build','block','adv-build', 'adv-block','random']
p2Chrome = Chromosome(['build','block','adv-build','adv-block','random'],intervals).getStrats() # all possible chromosomes
filehandler = open('GraphList_n15_L1000.obj', 'r') 
graphList = pickle.load(filehandler) # list of 1000 random graph objects

'''----------------------------------GRAPH GLOBALS----------------------------------------'''


n = 15 # number of nodes
# incase fixed
fixed = True # make is much quicker



'''----------------------------------EVOLUTION----------------------------------------'''

'''Evolution for player 1: 'red' '''
def play(chromosome):
    strats = []
    for c in chromosome:
        strats.append(chrome[c])
    if fixed:
        g.resetFixed()
    else:
        graphList[rand.randint(0,len(graphList)-1)] # get random graph
    player1 = Player(0, g) # red
    player2 = Player(1, g) # blue
    
    player1.setStrats(strats) # set strat list as well as initial strategy
    player2.setStrats(p2Chrome[random.randint(0,len(p2Chrome)-1)])
    
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

        else: # player 2 goes first
            if g.done(): # stop
                break
            player2.play()
            g.checkInterval(player1, player2)
                
            if g.done(): # stop
                break

            player1.play()
            g.checkInterval(player1, player2)

    return g.winner()

#    
def evalFunc(chromosome):
    best.append(ga.bestIndividual()) # record best individual at fitness call
    score = 0.0
    for g in range(10):
        result = play(chromosome)
        if result == "red":
            score+=1.0
    return score


        

def edit(string):
    idx = string.find("List:		 ")+9 # find index of first [
    idx2 = string[idx:].find("]")
    nString = string[idx:idx+idx2]
    return nString.replace(" ","").split(",")


def getBest():
    short = []
    #for i in range(popSize-1,(nGens+1)*popSize,popSize):
    for i in range((nGens+1)*popSize):
        if i%(popSize)==(popSize-1):
            s = edit(str(best[i]))
            short.append(s)
    return short

def mainEvol():
    global g
    g = Graph(n)
    g.setInterval(intervals)
    g.prep() # reset graph and prep triangles


    genome = G1DList.G1DList(intervals) # create random list of numbers
    genome.evaluator.set(evalFunc) #pass in fitness function
    genome.setParams(rangemin=0, rangemax=len(chrome)-1) #set range for numbers
    global ga
    global best
    global popSize
    global nGens
    
    
    
    best = []
    popSize = 100
    nGens = 15
    #genome.crossover.set(Crossovers.G1DListCrossoverUniform)
    genome.crossover.set(Crossovers.G1DListCrossoverTwoPoint)
    genome.mutator.set(Mutators.G1DListMutatorSwap)
    ga = GSimpleGA.GSimpleGA(genome)

    ga.setPopulationSize(popSize) # defaults to 80
    ga.setGenerations(nGens) # nGens + 1
    ga.evolve(freq_stats=10)

    short = getBest()
    print(short)

            


    #print(ga.bestIndividual())
    #print(genome)

mainEvol()
