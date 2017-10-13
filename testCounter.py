'''
testCounter.py
testing function for triangle detection

'''
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
    n3 = g.getNode(3)
    n4 = g.getNode(4)
    n5 = g.getNode(5)


    g.addEdge(n0,n1)
    g.addEdge(n1,n2)
    g.addEdge(n2,n0)
    g.addEdge(n2,n3)
    g.addEdge(n3,n4)
    g.addEdge(n3,n5)
    g.addEdge(n4,n5)



def depth2(node, level):
    print(node.ID)
    node.visit()
    nodes = node.neighbors
    if level==2:
        print("end")
    if level<2:
        for n in nodes:
            if not n.visited:
                
                if n.getDegree()>1:
                    depth(n, level+1)
            

def depth(sNode, node, level, tri):
    nodes = node.neighbors
    if level==2 and sNode in nodes:
       print("found triangle")
       printTri(tri)
    if level<2:
        for n in nodes:
            print("head:",node.ID)
            printTri(nodes)
            print()
            #print(node.ID)
            #print()
            #print(n.ID)
            tri.append(n)
            if n.getDegree()==1:
                node.visit()
            elif not n.visited:
                node.visit()
                depth(sNode, n, level+1, tri)

def printTri(tri):
    for n in tri:
        print(n.ID)
                              


def main():
    global g
    g = Graph(6)
    testG1(g)
    
    for i in range(6):
        depth(g.getNode(i), g.getNode(i), 0, [])


    



main()
