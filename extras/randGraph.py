'''
Testing function for random graph generator


'''


from __future__ import absolute_import, division, print_function
import sys, os
from Graph import *
from IterRamsey import *
import random as rand
sys.path.append(os.path.abspath('../pyevolve'))
from pyevolve import *
import random

def randomize(graph):
    n = graph.nNodes
    # generate random edge count 
    # n-1 is a tree// n*(n-1)/2 is a complete graph
    total = random.randint(n-1,n*(n-1)/2)
    print(total)

    while(total!=0): # add edge in randomly until empty
        n1 = random.randint(0,n-1)
        n2 = random.randint(0,n-1)
        # TODO use a hashmap to fix this
        # mapping unique to natural numbers using primes 
        while((n1==n2) or (graph.isEdge(graph.getNode(n1), graph.getNode(n2))==True)): # no nodes connected to themselves 
            n1 = random.randint(0,n-1)
            n2 = random.randint(0,n-1)
        graph.addEdge(graph.getNode(n1),graph.getNode(n2))
        total-=1
    return graph



            

def main():
    nNodes = 5
    g = Graph(nNodes)
    g.randomize()
    g.printGraph()



main()
