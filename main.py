'''main.py
program to start playing some games with graphs and iter classes

'''
from __future__ import absolute_import, division, print_function
import sys, os
from Graph import *
from IterRamsey import *
import random as rand
sys.path.append(os.path.abspath('../pyevolve'))
from pyevolve import *

def testGraph(g):
    n0 = g.getNode(0)
    n1 = g.getNode(1)
    n2 = g.getNode(2)
    n3 = g.getNode(3)
    n4 = g.getNode(4)
    n5 = g.getNode(5)
    n6 = g.getNode(6)
    n7 = g.getNode(7)
    n8 = g.getNode(8)
    n9 = g.getNode(9)
    
    g.addEdge(n0, n1)
    g.addEdge(n0, n2)
    g.addEdge(n0, n3)
    g.addEdge(n1, n2)
    g.addEdge(n1, n4)
    g.addEdge(n2, n4)
    g.addEdge(n2, n6)
    g.addEdge(n2, n3)
    g.addEdge(n2, n5)
    g.addEdge(n3, n5)
    g.addEdge(n5, n6)
    g.addEdge(n4, n6)
    return g

def playGame():
    nNodes = 10
    g = Graph(nNodes)
    g = testGraph(g)
    player1 = IterRamsey(0, g)
    player2 = IterRamsey(1, g)
    wins = 10000

    # temp variable
    # game loop
    while(True):
        if g.done():
            #TEMPORARY CODE FOR TESTING
            r = rand.uniform(0,1)
            if r>.5:
                wins = 1
            else:
                wins = 0
            #END OF TEMPORARY CODE
            break
        player1.play()
        player2.play()
        

    print("player",wins,"wins")
    return wins

############################TESTING PORTION###################################





        
###############################################################################
##########################EVOLVING PORTION OF CODE#############################
###############################################################################
def fitness(chromosome):
    print(chromosome)
    score = 0.0
    # plays game once; trying to evolve player 1 
    result = playGame()
    if result == 0:
        score+=1.0
    return score


def mainEvolve():
    genome = G1DList.G1DList(10)
    genome.evaluator.set(fitness)
    ga = GSimpleGA.GSimpleGA(genome)
    ga.evolve(freq_stats=10)
    
