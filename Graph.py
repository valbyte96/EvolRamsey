''' Graph.py
@author: Ted McCulloch
@version: 9/23/17
Graph.py contains three separate classes:
>Node
>Edge
>Graph

'''
from __future__ import absolute_import, division, print_function
import sys, os
import random


'''Node Class'''
class Node:
    def __init__(self, ID):
        '''Constructor
        @params ID: unique numerical identifier for each node
        >neighbors: initialize empty list of neighbors
        >visited: node's status of whether or not it's been visited'''
        self.ID = ID 
        self.neighbors = [] 
        self.visited = False
    def addNeighbor(self, neigh):
        '''@param neigh: node that is connected to this node via edge
        adds neighbors to running list contained in Node class'''
        self.neighbors.append(neigh)
    def getDegree(self):
        '''returns degree'''
        return len(self.neighbors)
    def visit(self):
        '''marks node as visited'''
        self.visited = True

'''Edge Class'''
class Edge:
    def __init__(self, n1, n2):
        '''Constructor
        @params n1, n2: two node objects such that n1!=n2
        >color: specifies color of edge; defaults to black
        >L: List for storing node objects'''
        self.color = "black" # default
        self.L = [n1, n2]
    def getColor(self):
        '''returns current color'''
        return self.color
    def setColor(self, color):
        '''@param color: new color
        use to change edge object's color '''
        self.color = color
    def isColored(self): # redundant method? 
        '''returns is colored'''
        if self.color == "black":
            return False
        else:
            return True
                  
'''Graph Class'''
class Graph:
    def __init__(self, nNodes):
        '''Constructor
        @params nNodes: number of nodes
        >neighbors: TODO
        >nodeList: record of nodes
        >edgeList: record of edges
        >cCount: counts the number of edges colored
        '''
        self.nNodes = nNodes
        self.nodeList = []
        self.edgeList = []
        self.cCount = 0 
        '''adds nodes specified'''
        for i in range(nNodes):
            self.addNode(i)

    def addNode(self, i): 
        '''@params i: ID number for new node'''
        self.nodeList.append(Node(i))

    def addEdge(self, n1, n2):
        '''@params n1, n2: Nodes attached by new edge
        method records two nodes as neibhors and adds edge to edge list'''
        n1.addNeighbor(n2) 
        n2.addNeighbor(n1)
        self.edgeList.append(Edge(n1, n2)) 
    def incColor(self):
        '''increments the counter for number of edges colored'''
        self.cCount+=1
    def done(self):
        '''indicates whether or not all edges are colored'''
        if self.cCount == len(self.edgeList):
            return True
        return False
    def getNode(self, ID):
        '''@params ID: node ID number
        returns node object based on node ID'''
        return self.nodeList[ID]
    def getEdges(self): # necessary? 
        '''method returns edgeList'''
        return self.edgeList
    def isEdge(self, x, y):
        '''@param x,y: distinct nodes
        method indicates if an edge exists between these two nodes'''
        b = False
        for e in self.edgeList: # HASHMAP?
            if (x in e.L and y in e.L):
                b = True
        return b
                

    def printGraph(self):
        '''Displays graph information'''
        print("Node IDs")
        for n in self.nodeList:
            print(n.ID)
        print("Edges by Node IDs")
        for e in self.edgeList:
            print(str(e.L[0].ID)+" "+str(e.L[1].ID))
    def randomize(self):
        '''method randomizes graph
        >total: calculates the number of edges in graph
                n-1 is a tree
                n*(n-1)/2 is a complete graph'''
        self.reset()
        n = self.nNodes
        total = random.randint(n-1,n*(n-1)/2)
        '''nested loops ensure no nodes linked to themselves and no repeat edges'''
        while(total!=0):
            n1 = random.randint(0,n-1)
            n2 = random.randint(0,n-1)
            while(n1==n2 or self.isEdge(self.getNode(n1), self.getNode(n2))):
                n1 = random.randint(0,n-1)
                n2 = random.randint(0,n-1)
            self.addEdge(self.getNode(n1),self.getNode(n2))
            total-=1
        return self            
    def reset(self):
        '''removes all edges and readds nodes to reset to blank graph'''
        del self.nodeList[:]
        del self.edgeList[:]
        self.cCount = 0 
        '''add in the specified nodes'''
        for i in range(self.nNodes):
            self.addNode(i)
            


#<--------------------------METHODS IN DEVELOPMENT-------------------------------->






    
