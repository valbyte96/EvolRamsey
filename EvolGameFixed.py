from __future__ import absolute_import, division, print_function
'''---------------------------------EvolGameFixed.py----------------------------------------
Evolution happens on a fixed graph defined at the beginning or
a graph that was previously pickled. 

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
import copy

'''----------------------------------GAME GLOBALS----------------------------------------'''
intervals = 5 # number of game intervals
chrome = ['build','block','adv-build', 'adv-block','random']
p2Chrome = Chromosome(['build','block','adv-build','adv-block','random'],intervals).getStrats() # all possible chromosomes

# IF YOU WANT PICKLED FIXED GRAPHS
filehandler = open('GraphList_n15_L3.obj', 'r') 
graphList = pickle.load(filehandler) # list of random graph objects
'''----------------------------------GRAPH GLOBALS----------------------------------------'''


n = 15 # number of nodes
idx = rand.randint(0,len(graphList)-1)
g = graphList[0] # pick first of pickled
g.setInterval(intervals)
g.prep() # reset graph and prep triangles




'''----------------------------------EVOLUTION----------------------------------------'''

'''Evolution for player 1: 'red' '''
def play(chromosome):
    strats = []
    for c in chromosome:
        strats.append(chrome[c])
    
    #g = graphList[idx]
    #g = copy.deepcopy(resetGraph)
    
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
    winner = g.winner()
    g.resetFixed()
    return winner

#    
def evalFunc(chromosome):
    best.append(ga.bestIndividual()) # record best individual at fitness call
    score = 0.0
    for i in range(1000):
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
    genome = G1DList.G1DList(intervals) # create random list of numbers
    genome.evaluator.set(evalFunc) #pass in fitness function
    genome.setParams(rangemin=0, rangemax=len(chrome)-1) #set range for numbers
    global ga
    global best
    global popSize
    global nGens
    
    
    
    best = []
    popSize = 80
    nGens = 20
    #genome.crossover.set(Crossovers.G1DListCrossoverUniform)
    genome.crossover.set(Crossovers.G1DListCrossoverTwoPoint)
    #genome.mutator.set(Mutators.G1DListMutatorSwap)
    genome.mutator.set(Mutators.G1DListMutatorIntegerRange)
    #genome.mutator.setParams(rangemin=0,rangemax=)
    ga = GSimpleGA.GSimpleGA(genome)

    ga.setPopulationSize(popSize) # defaults to 80
    ga.setGenerations(nGens) # nGens + 1
    ga.evolve(freq_stats=10)

    short = getBest()
    print(short)

            


    #print(ga.bestIndividual())
    #print(genome)


def nEvol():
    iterations = 4
    global g
    g = graphList[0] # pick first of pickled
    g.setInterval(intervals)
    g.prep() # reset graph and prep triangles
    g.defUnit()

    final = []

    

    for i in range(iterations):
        print("iteration:",i+1)
        genome = G1DList.G1DList(intervals) # create random list of numbers
        genome.evaluator.set(evalFunc) #pass in fitness function
        genome.setParams(rangemin=0, rangemax=len(chrome)-1) #set range for numbers
        global ga
        global best
        global popSize
        global nGens
        
        
        
        best = []
        del best[:] # empty best

        popSize = 80
        nGens = 20
        genome.crossover.set(Crossovers.G1DListCrossoverTwoPoint)
        #genome.mutator.set(Mutators.G1DListMutatorIntegerRange)
        genome.mutator.set(Mutators.G1DListMutatorSwap)
        ga = GSimpleGA.GSimpleGA(genome)

        ga.setPopulationSize(popSize) # defaults to 80
        ga.setGenerations(nGens) # nGens + 1


        ga.evolve(freq_stats=20)
        short = getBest()
        print(short)
        final.append(short[len(short)-1])
    print()
    print(final)

            


    #print(ga.bestIndividual())
    #print(genome)

mainEvol()
#nEvol()
