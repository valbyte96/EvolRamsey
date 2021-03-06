from __future__ import absolute_import, division, print_function
'''---------------------------------evolGame.py----------------------------------------
evolution happens here'''

'''---------------------------------IMPORTS----------------------------------------'''
import sys, os
from Graph import *
from Player import *
from Chromosome import *
import random as rand
sys.path.append(os.path.abspath('../pyevolve'))
from pyevolve import *
'''----------------------------------GLOBALS----------------------------------------'''
intervals = 2 # number of game intervals
chrome = Chromosome(['build','block','random'],intervals).getStrats() # all possible chromosomes
#chrome = Chromosome(['build'],intervals).getStrats() # all possible chromosomes
#chrome = [('build', 'build'), ('build', 'block')]
print(chrome)
n = 16 # number of nodes
g = Graph(n) # global graph
new = False # boolean if want to create a new graph which each game
count = 0
'''----------------------------------EVOLUTION----------------------------------------'''

'''Evolution for player 1: 'red' '''
def play(strats):
    g = Graph(n)
    g.setInterval(intervals)
    if(new): # new graph with each game
        g = Graph(n) 
    g.prep() # reset graph and prep triangles
    player1 = Player(0, g) # red
    player2 = Player(1, g) # blue
    
    player1.setStrats(strats) # set strat list as well as initial strategy
    player2.setStrats(chrome[random.randint(0,len(chrome)-1)])
    
    r = 0 # debug
    unit = g.getNumEdges()/intervals
    
    
    while(True):
        if g.done(): # stop
            break
        player1.play()
        g.checkInterval(player1, player2)
            
        if g.done(): # stop
            break

        player2.play()
        g.checkInterval(player1, player2)
        r+=1 # debug

    return g.winner()

    
def evalFunc(chromosome):
    global count
    count+=1
    score = 0.0
    for c in chromosome:
        #print(c)
        result = play(chrome[c])
        if result == "red":
            score+=1.0
    #print("here")
    return score

def testMain():
    print(play(["build","build"]))


def mainEvol():
    genome = G1DList.G1DList(3)
    genome.evaluator.set(evalFunc) #pass in fitness function
    genome.setParams(rangemin=0, rangemax=len(chrome)-1)
    ga = GSimpleGA.GSimpleGA(genome)
    ga.setGenerations(2)
    ga.evolve(freq_stats=2)
    print(ga.bestIndividual())

mainEvol()
#testMain()
