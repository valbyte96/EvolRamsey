''' Graph.py
@author: Ted McCulloch
@version: 9/23/17
Underlying graph class for playing Ramsey games
'''
from __future__ import absolute_import, division, print_function
import sys, os


'''Node Class'''
class Node:
    def __init__(self, ID):
        self.ID = ID
        self.neighbors = [] #TODO: implement a list of neighbors
        self.visited = False

    def addNeighbor(self, neigh):
        self.neighbors.append(neigh)

    def getDegree(self):
        return len(self.neighbors)
    def visited(self):
        self.visited = True

'''Edge Class'''
class Edge:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.color = "black"

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color
    def isColored(self):
        if self.color == "black":
            return False
        else:
            return True
                  
'''Graph Class'''
class Graph:
    def __init__(self, nNodes):
        self.nNodes = nNodes
        self.neighbors = {} # dictionary: keys = nodes; values = neighbors
        self.nodeList = []
        self.edgeList = []
        self.cCount = 0 # counts the number of edges colors with any color
        # add in the specified nodes
        for i in range(nNodes):
            self.addNode(i)

    def addNode(self, i):
        node = Node(i)
        self.nodeList.append(node)

    def addEdge(self, n1, n2):
        edge = Edge(n1, n2) # create edge
        n1.addNeighbor(n2) # record new neighbors
        n2.addNeighbor(n1)
        self.edgeList.append(edge) # record new edge

    def incColor(self):
        self.cCount+=1
    def done(self):
        if self.cCount == len(self.edgeList):
            return True
        return False
    def getNode(self, ID):
        return self.nodeList[ID]
    def getEdges(self):
        return self.edgeList

    # METHODS IN DEVELOPMENT/ UNTESTED
    def randomize(self):
        self.reset() # reset graph first

    # resets graph to initial state
    # probably doesn't work (TODO)
    def reset(self):
        self.neighbors = {} # dictionary: keys = nodes; values = neighbors
        self.nodeList = []
        self.edgeList = []
        self.cCount = 0 # counts the number of edges colors with any color
        # add in the specified nodes
        for i in range(nNodes):
            self.addNode(i)
    
    
    
    # TESTING CLASSES

    
    def printNodes(self):
        for n in self.nodeList:
            print(n.ID)
        
    




    
