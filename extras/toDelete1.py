from __future__ import absolute_import, division, print_function
import sys, os
from Graph import *
from IterRamsey import *
import random as rand
sys.path.append(os.path.abspath('../pyevolve'))
from pyevolve import *

T = []
n = 0

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
    if level>2:
        print("end")
    else:

        for n in nodes:
            if not n.visited: # skip visited nodes and leaves
                n.visit() # mark as visited
                if n.getDegree()>1:
                    print(n.ID)
                    findT(graph, n, level+1)


def depth(graph, sNode, node, level):
    nodes = node.neighbors
    if level>0 and sNode == node:
        n+=1
    elif level < 3:
        for n in nodes:
            if not n.visited: # skip visited nodes and leaves
                print("here")
                n.visit() # mark as visited
                if n.getDegree()>1:
                    print(n.ID)
                    findT(graph, n, level+1)        
    
            
    
    


def main():
    global g
    global n
    g = Graph(3)
    findT(g, g.getNode(0), 0)
 #   depth(g,g.getNode(0), g.getNode(0), 0)


    



main()
