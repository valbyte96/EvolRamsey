from __future__ import absolute_import, division, print_function
'''


'''
import cPickle as pickle
filehandler = open('GraphList_n15_L3.obj', 'r') 
graphList = pickle.load(filehandler)

print(len(graphList[0].edgeList))
print(len(graphList[1].edgeList))
print(len(graphList[2].edgeList))
