from __future__ import absolute_import, division, print_function
import sys, os
from Graph import *
from DGraph import *
from Player import *
import random as rand
sys.path.append(os.path.abspath('../pyevolve'))
from graphics import *
import math


WIDTH = 500
HEIGHT = 500
n = 6

g = Graph(n)
n1, n2, n3, n4, n5, n6 = g.nodeList

g.addEdge(n1, n2)

g.addEdge(n1, n3)
g.addEdge(n1, n4)
g.addEdge(n1, n5)
g.addEdge(n1, n6)
g.addEdge(n2, n3)
g.addEdge(n2, n4)
g.addEdge(n2, n5)
g.addEdge(n2, n6)
g.addEdge(n3, n4)
g.addEdge(n3, n5)
g.addEdge(n3, n6)
g.addEdge(n4, n5)
g.addEdge(n4, n6)
g.addEdge(n5, n6)

eList = g.edgeList



win = GraphWin('Ramsey', WIDTH, HEIGHT)
graph = DGraph(g, win, WIDTH/2, HEIGHT/2)
graph.drawCircle()
for e in eList:
    r = rand.randint(0,1)
    if r == 0:
        e.drawEdge(win,r)
    else:
        e.drawEdge(win,r)



# display


