'''---------------------------------DGraph.py----------------------------------------
A wrapper class for the graph class.
Considering phasing out and combining with the regular graph class.
Essentially handles main graphics for the graph'''
'''---------------------------------IMPORTS----------------------------------------'''
from graphics import *
import math
import random as rand
'''----------------------------------GLOBALS----------------------------------------'''
colors = ['red', 'blue']
'''-----------------------------------CLASS----------------------------------------'''
class DGraph:
    def __init__(self, graph, win, x, y):
        '''params graph, win, x, y:
        graph class, graphics window, x-center, y-center'''
        self.graph = graph
        self.graph.setWin(win)
        self.r = 100 # radius
        self.x = x
        self.y = y
        self.c = 5 # small circle radius
        self.d_rads = 6.28319 / len(graph.nodeList)  # change in radians (2pi/n)
        self.win = win
        self.nodes = graph.nodeList
        self.edges = graph.edgeList

    def getEdge(self, n1, n2):
        '''params n1, n2: return edge between two nodes'''
        return self.graph.getEdge(n1,n2)
    def getRand(self):
        '''get two random, distinct nodes that form an existant and available edge'''
        L = len(self.nodes)-1
        while True:
            r1 = rand.randint(0, L)
            r2 = rand.randint(0, L)
            while r1 == r2:
                r2 = rand.randint(0, L)
            if self.graph.getEdge(self.nodes[r1], self.nodes[r2])!=False:
                return self.nodes[r1], self.nodes[r2]
    def isTouched(self, checkPoint):
        '''param checkPoint: clicked point
        checks to see if mouse click is within a node'''
        win = self.win
        x = checkPoint.getX()
        y = checkPoint.getY()
        c = 5 #TODO: connect between files
        for n in self.nodes:
            
            n_x = n.center.getX()
            n_y = n.center.getY()
            if x > n_x - c and x < n_x + c and y > n_y - c and y < n_y + c:
                n.setColor('green')
                n.redraw(win)
                return True, n
        return False, None
    def draw(self):
        '''intial draw for graph. Also responsible for assigning lines
        to edges'''
        win = self.win
        # draw nodes
        R = self.r
        rad = 0
        '''<---draw nodes--->'''
        for n in self.nodes:
            x = R * math.cos(rad) + self.x
            y = R * math.sin(rad) + self.y
            n.setCenter(Point(x,y))
            n.draw(win)
            rad += self.d_rads
        '''<---draw edges--->'''
        for e in self.edges:
            p1, p2 = e.getPoints()
            line = Line(p1,p2)
            line.setFill('black')
            e.setLine(line) # store lines
            line.draw(win)
    def drawEdge(self, edge, team):
        '''params edge, team: specified edge to redraw, team's ID to specify color'''
        line = edge.getLine()
        line.undraw()
        line.setFill(colors[team])
        line.draw(self.win)
    def check(self, player):
        '''param player: given player that you want to strategy switch for
        checks the progress of graph'''
        if self.graph.cCount >=self.graph.check:
            self.graph.check+=self.graph.unit
            self.graph.strat+=1
            print("STRAT CHANGE") # testing statement
            player.setStrat(self.graph.strat)
        
            
        

