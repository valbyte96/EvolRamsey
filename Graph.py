from __future__ import absolute_import, division, print_function
''' Graph.py
@author: Ted McCulloch
@version: 11/27/17
Graph.py contains three separate classes:
>Node
>Edge
>Graph
>Triangle

'''
'''---------------------------------IMPORTS----------------------------------------'''
from graphics import *
import sys, os
import random
'''---------------------------------GLOBALS-----------------------------------------'''
colors = ['red', 'blue']
'''--------------------------------NODE CLASS-------------------------------------'''
class Node:
    def __init__(self, ID):
        '''Constructor
        @params ID: unique numerical identifier for each node
        >neighbors: initialize empty list of neighbors
        >visited: node's status of whether or not it's been visited'''
        self.ID = ID 
        self.neighbors = [] 
        self.visited = False
        '''<---for graphics--->'''
        self.center = None
        self.circle = None
        self.r = 5
        self.color = "black" #default to black
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
    '''<---for graphics--->'''
    def setCenter(self, point):
        self.center = point
        self.circle = Circle(point, self.r)
    def setColor(self, color):
        self.color = color        
    def draw(self, win):
        self.circle.setFill(self.color)
        self.circle.draw(win)
    def redraw(self, win):
        self.circle.setFill(self.color)
        self.circle.undraw()
        self.circle.draw(win)
'''--------------------------------EDGE CLASS-------------------------------------'''
class Edge:
    def __init__(self, n1, n2):
        '''Constructor
        @params n1, n2: two node objects such that n1!=n2
        >color: specifies color of edge; defaults to black
        >L: List for storing node objects'''
        self.color = "black" # default
        self.L = [n1, n2]
        self.notColored = 1
        self.line = None # line associated with edge
    def contains(self, x, y):
        '''Given two nodes'''
        if x in self.L and y in self.L:
            return True
        return False
    def getColor(self):
        '''returns current color'''
        return self.color
    def setColor(self, color):
        '''@param color: new color
        use to change edge object's color '''
        self.color = color
        self.notColored = 0
    def isColored(self): # redundant method? 
        '''returns is colored'''
        if self.color == "black":
            return False
        else:
            return True
    '''<---for graphics--->'''
    def getPoints(self):
        '''returns the two center points for nodes associated
        with the edge'''
        return self.L[0].center, self.L[1].center
    def setLine(self, line):
        '''@param line: line object
        store the line associated with this edge'''
        self.line = line
    def getLine(self):
        '''return the line associated with this edge'''
        return self.line
    def drawEdge(self, win, ID):
        '''@params win, ID: window that edge is draw, player ID to specify color
        function redraws edge with correct color'''
        self.setColor(colors[ID]) # increments cCount and updates class params
        line = self.getLine()
        line.undraw()
        line.setFill(colors[ID])
        line.draw(win)
                  
'''--------------------------------GRAPH CLASS-------------------------------------'''
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
        self.nodeList  = []
        self.edgeList  = []
        self.triangles = []
        self.cCount = 0
        self.intervals = 3 # default to three
        self.verbose = 0
        self.unit = 0 # unit size; TODO: best default?
        self.check = 0
        self.strat = 0
        self.win = None
        
        
        '''adds nodes specified'''
        for i in range(nNodes):
            self.addNode(i)
    def prep(self):
        '''Given a graph on n nodes, randomize, count, and define units'''
        self.randomize()
        self.countT()
        self.unit = self.getNumEdges()/self.intervals
        self.check = self.unit
    def check(self, p1, p2):
        if self.cCount >=self.check:
            self.check+=self.unit
            self.strat+=1
            p1.setStrat(self.strat)
            p2.setStrat(self.strat)     
    def setInterval(self, n):
        '''setter method for number of intervals'''
        self.intervals = n
    def setVerbose(self, n):
        self.verbose = n
    def setUnit(self, unit):
        print(unit)
        self.unit = unit

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
   # def getEdge below
        
        
    def getEdges(self): # necessary? 
        '''method returns edgeList'''
        return self.edgeList
    def isEdge(self, n1, n2):
        '''@param n1,n2: distinct nodes
        method indicates if an edge exists between these two nodes'''
        b = False
        for e in self.edgeList: # HASHMAP?
            if e.contains(n1,n2):
                b = True
        return b
    def getNumEdges(self):
        '''method returns the number of edges in this graph'''
        return len(self.edgeList)
    def getNumTri(self):
        '''method returns the number of triangles in graph'''
        return len(self.triangles)
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
        total = random.randint(n+1,n*(n-1)/2)
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
    def setWin(self, win):
        '''param win: graphics window class
        method stores/initializes graphics window'''
        self.win = win
#<------------------------------IN DEVELOPMENT-------------------------------->
    def winner(self):
        '''returns color of winner'''
        c1 = 0
        c2 = 0
        for t in self.triangles:
            if t.isMono():
                e = t.edges[0].color
                if e =='blue':
                    c1+=1
                elif e =='red':
                    c2+=1
        if c1>c2:
            if self.verbose>0:
                print('red',c2)
                print('blue',c1)
            return 'blue'
        elif c1<c2:
            if self.verbose>0:
                print('red',c2)
                print('blue',c1)
            return 'red'
        else:
            if self.verbose>0:
                print('red',c2)
                print('blue',c1)
        return 'tie game'            
    
    def getEdge(self, n1, n2):
        '''@params n1, n2: two nodes making up an edge
        if edge exists, returns it, else returns false'''
        for e in self.edgeList: # HASHMAP?
            if e.contains(n1,n2):
                return e
        return False
    def getPercent(self):
        '''returns the a number between 0 and 1; represents the percent
        of edges colored. Method used for strategy switching'''
        return self.cCount/len(self.edgeList)
    
    def countT(self):
        '''Method for counting the number of triangles in the graph.
        Method tests each edge (x,y) to see if there exists a node n such that
        there is a triangle xy yn xn. 
        Notes:
            >O(n^3)
            >Look into optimizing this'''
        T = [] # prevents overcounting
        for e in self.edgeList:
            x = e.L[0]
            y = e.L[1]
            for n in self.nodeList:
                if n==x or n==y:
                    continue
                elif self.isEdge(x,n) and self.isEdge(y,n):
                    L = [x, y, n]
                    L.sort()
                    if L not in T:
                        T.append(L)
                        self.triangles.append(Triangle(self, x,y,n))
        if self.verbose>0:
            print(len(self.triangles))
    

        
            

'''--------------------------------TRIANGLE CLASS-------------------------------------'''           
class Triangle:
    '''Constructor'''
    def __init__(self, g, n1, n2, n3):
        self.nodes = [n1, n2, n3]
        self.edges = [g.getEdge(n1,n2), g.getEdge(n1,n3), g.getEdge(n3,n2)]


    def isFull(self):
        '''Method returns True if all edges colored in'''
        e = self.edges;
        if e[0].isColored() and e[1].isColored() and e[2].isColored():
            return True
        return False
    def isMono(self):
        '''Method returns True if triangle in a single color'''
        c = self.edges[0].color
        for e in self.edges:
            if e.color != c:
                return False
        return True
    def singleC(self, color):
        '''Method returns True if a triangle is only color and black'''
        for e in self.edges:
            if e.color!="black" and e.color!= color:
                return False
        return True
    def antiSingleC(self,color):
        '''for blocking method'''
        for e in self.edges:
            if e.color!="black" and e.color== color:
                return False
        return True
        
        
    def available(self):
        '''Method returns the number of edges available to be colored'''
        e = self.edges;
        return e[0].notColored + e[1].notColored + e[2].notColored
    def getAvailable(self):
        '''Method returns an available edge to be colored;
           if no edge exists it returns 0.'''
        for e in self.edges:
            if e.notColored == 1:
                return e
        return 0

    
        




    
