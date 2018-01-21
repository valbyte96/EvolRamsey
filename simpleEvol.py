from __future__ import absolute_import, division, print_function
'''simpleEvol.py
A simple example of evolutionary computation using pyevolve.
Simply for familiarizing me with pyevolve

'''
# Libraries
import sys, os
sys.path.append(os.path.abspath('../pyevolve'))

from pyevolve import *

def eval_func(chromosome):
      score = 0.0
      print(chromosome)
      # iterate over the chromosome elements (items)
      for value in chromosome:
         if value==0:
            score += 1.0
      return score

def main():
    # Tell Python what your genome looks like
    n=10
    genome = G1DList.G1DList(n) #20 ints
    
    # tell Python what fitness function is 
    genome.evaluator.set(eval_func) #pass in fitness function
    genome.setParams(rangemin=0, rangemax=n-1)

    # create genetic algorithm enguine 
    ga = GSimpleGA.GSimpleGA(genome)
    
    # run the evolutionary process
    ga.evolve(freq_stats=10) #runs ge; reports every 10 gens
    print(ga.bestIndividual())

main()
