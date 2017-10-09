'''simpleEvol.py
A simple example of evolutionary computation using pyevolve.
Simply for familiarizing me with pyevolve

'''
# Libraries
from __future__ import absolute_import, division, print_function
import sys, os
sys.path.append(os.path.abspath('../pyevolve'))

from pyevolve import *

def eval_func(chromosome):
      score = 0.0
      # iterate over the chromosome elements (items)
      for value in chromosome:
         if value==0:
            score += 1.0
      return score

def main():
    # Tell Python what your genome looks like
    genome = G1DList.G1DList(30) #20 ints
    
    # tell Python what fitness function is 
    genome.evaluator.set(eval_func) #pass in fitness function

    # create genetic algorithm enguine 
    ga = GSimpleGA.GSimpleGA(genome)
    
    # run the evolutionary process
    ga.evolve(freq_stats=10) #runs ge; reports every 10 gens

main()
