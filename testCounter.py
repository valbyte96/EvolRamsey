from __future__ import absolute_import, division, print_function
import sys, os
from Graph import *
from IterRamsey import *
import random as rand
sys.path.append(os.path.abspath('../pyevolve'))
from pyevolve import *

T = []

# just a triangle
def testG1(g):
    n0 = g.getNode(0)
    n1 = g.getNode(1)
    n2 = g.getNode(2)

    g.addEdge(n0,n1)
    g.addEdge(n1,n2)
    g.addEdge(n2,n0)




# find triangles recursively
def findT(graph, node, level):
    nodes = node.neighbors

    for n in nodes:
        if not n.visted: # skip visited nodes and leaves
            n.visited() # mark as visited
            if n.getDegree()>1:
                findT(graph, n, level+1)
            
    
    


def main():
    global g
    g = Graph(3)
    testG1(g)
    findT(g)


    



main()
