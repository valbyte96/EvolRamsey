from __future__ import absolute_import, division, print_function
import sys, os
from Graph import *
from Player import *
import random as rand
sys.path.append(os.path.abspath('../pyevolve'))
from pyevolve import *


def evalFunc(chromosome):
    score = 0.0
    for c in chromosome:
        if c==0:
            score+=1
    return score


def main():
    genome = G1DList.G1DList(2)
    genome.evaluator.set(evalFunc) #pass in fitness function
    genome.setParams(rangemin=0, rangemax=8)
    ga = GSimpleGA.GSimpleGA(genome)
    ga.evolve(freq_stats=10)
    print(ga.bestIndividual())
    
    




main()
