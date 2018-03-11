from __future__ import absolute_import, division, print_function
'''GraphGen.py
this file generates and pickles graph objects in order to increase runtime
of evolving code'''

import cPickle as pickle
from Graph import *
n = 15
L = 3
intervals = 500
graphList = []


for i in range(L):
    g = Graph(n)
    g.setInterval(intervals)
    g.prep() # causing trouble
    graphList.append(g)


#fObj = open('GraphList_n15_L3.obj', 'w')
#pickle.dump(graphList, fObj)

with open("GraphList_n15_L3.obj", "wb") as f:
    pickle.dump(graphList, f)
