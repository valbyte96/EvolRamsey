''' IterRamsey.py
@author: Ted McCulloch
@version: 9/23/17
Class for implementing an iterative player, which will perform with
consistent strategies. 
'''
from __future__ import absolute_import, division, print_function
import sys, os
import random as rand

colorList = ['red', 'blue']

class IterRamsey:
    def __init__(self, ID, graph):
        self.ID = ID
        self.strat = "random"
        self.graph = graph
        self.color = colorList[ID]

    
    def play(self):
        if self.strat == "random":
            self.randomStrat()
            
    def randomStrat(self):
        edges = self.graph.getEdges()
        idx = len(edges) - 1
        r = rand.randint(0, idx)

        while(edges[r].isColored == False):
            r = rand.randint(0, idx)
            # WARNING: infinite loop if everything
        rEdge = edges[r]
        rEdge.setColor(self.color)
        self.graph.incColor()
            
