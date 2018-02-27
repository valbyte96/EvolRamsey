from __future__ import absolute_import, division, print_function
'''


'''
import cPickle as pickle
filehandler = open('GraphList_n15_L1000.obj', 'r') 
graphList = pickle.load(filehandler)

print(len(graphList))
