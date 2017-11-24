'''DGraph.py ~ drawable graph class'''
from graphics import *
import math
import random

class DGraph:
    def __init__(self, graph, win, x, y):
        self.graph = graph
        self.r = 100 # radius
        self.x = x
        self.y = y
        self.c = 5 # small circle radius
        self.d_rads = 6.28319 / len(graph.nodeList)  # change in radians (2pi/n)
        self.win = win

        # CAUTION: how does this update? Pay attention
        self.nodes = graph.nodeList
        self.edges = graph.edgeList

    def getEdge(self, n1, n2):
        return self.graph.getEdge(n1,n2)

    def isTouched(self, checkPoint):
        win = self.win
        x = checkPoint.getX()
        y = checkPoint.getY()
        c = 5 #TODO: connect between files
        for n in self.nodes:
            
            n_x = n.center.getX()
            n_y = n.center.getY()
            if x > n_x - c and x < n_x + c and y > n_y - c and y < n_y + c:
                n.setColor('red')
                n.redraw(win)
                return True, n
        return False, None
    def draw(self):
        win = self.win
        # draw nodes
        R = self.r
        rad = 0
        for n in self.nodes:
            x = R * math.cos(rad) + self.x
            y = R * math.sin(rad) + self.y
            n.setCenter(Point(x,y))
            n.draw(win)
            rad += self.d_rads
        # draw edges
        for e in self.edges:
            p1, p2 = e.getPoints()
            line = Line(p1,p2)
            line.setFill('black')
            line.draw(win)
            
        

