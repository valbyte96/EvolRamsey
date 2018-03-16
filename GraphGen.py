from __future__ import absolute_import, division, print_function
'''GraphGen.py
this file generates and pickles graph objects in order to increase runtime
of evolving code'''

import cPickle as pickle
from Graph import *
import sys
n = 15
L = 1000
intervals = 5
graphList = []
sys.setrecursionlimit(1500)
#print(sys.getrecursionlimit())

for i in range(L):
    g = Graph(n)
    g.setInterval(intervals)
    g.prep() # causing trouble
    graphList.append(g)


#fObj = open('GraphList_n15_L3.obj', 'w')
#pickle.dump(graphList, fObj)

#with open("test.obj", "wb") as f:
#    pickle.dump(graphList, f)

with open("GraphList_n15_L1000.obj", "wb") as f:
    pickle.dump(graphList, f)
