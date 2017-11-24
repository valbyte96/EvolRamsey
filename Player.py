''' Player.py
@author: Ted McCulloch
@version: 10/21/17
Class for implementing an iterative player, which will perform with
consistent strategies. 
'''
from __future__ import absolute_import, division, print_function
import sys, os
import random as rand

colorList = ["red", "blue"]

class Player:
    def __init__(self, ID, graph):
        self.ID = ID
        self.strat = "random" # default to random
        self.graph = graph
        self.color = colorList[ID]
        self.stratList = []


    
    def play(self):
        if self.strat == "block":
            self.block()
        elif self.strat == "build":
            self.build()
        elif self.strat == "tri1":
            self.tri1Strat()
        elif self.strat == "random":
            self.random()
        else:
            if self.graph.verbose>0:
                print("Warning: strategy doesn't exist")
            self.random()
            
    def setStrat(self, num):
        if num<len(self.stratList):
            self.strat = self.stratList[num]
        else:
            print("warning: id number greater than interval number")
            self.strat = self.stratList[0]

    def setStrats(self, strats):
        '''Responsible for initializing list of strategies as well as first strategy'''
        self.stratList = strats
        self.strat = strats[0]

    def build(self): #very simple
        '''always build before anything else'''
        tri = self.graph.triangles
        s = 10
        sTri = [] 
        for t in tri:
            if not t.isFull() and t.singleC(self.color): # TIME
                '''get triangle that is not full and best for building'''
                n = t.available() 
                if n<s: # color in least available
                    s = n
                    sTri = t # save triangle
        if sTri!=[]:
            e = sTri.getAvailable()
            e.setColor(self.color)
            self.graph.incColor()
        else:
            # try another strategy
            if self.graph.verbose>0:
                print("build -> random")
 #           self.tri1Strat()
            self.random()
    

    def block(self): #simple
        '''always block before anything else'''
        tri = self.graph.triangles
        s = 10
        sTri = [] 
        for t in tri:
            if not t.isFull() and t.antiSingleC(self.color): # TIME
                '''get triangle that is not full and best for building'''
                n = t.available() 
                if n<s: # color in least available
                    s = n
                    sTri = t # save triangle
        if sTri!=[]:
            e = sTri.getAvailable()
            e.setColor(self.color)
            self.graph.incColor()
        else:
            # try another strategy
            if self.graph.verbose>0:
                print("block -> tri1")
            self.tri1Strat()
            #self.random()
        
        
    def tri1Strat(self):
        '''Always color in the most "available" triangle
            Doesn't take into account color yet'''
        tri = self.graph.triangles
        s = -10
        sTri = []
        
        for t in tri:
            if not t.isFull():
                n = t.available() #
                if n>s:
                    s = n
                    sTri = t # save triangle
        if sTri!=[]:
            e = sTri.getAvailable()
            e.setColor(self.color)
            self.graph.incColor()
        else:
            #print("stopping condition")
            self.graph.cCount = len(self.graph.edgeList)
                

 # TODO COMMENT           
    def random(self):
        b = 0
        full = False
        edges = self.graph.getEdges()
        idx = len(edges) - 1
        r = rand.randint(0, idx)

        while(edges[r].isColored == False):
            r = rand.randint(0, idx)
            b+=1
            if b>len(self.graph.edgeList)-2:
                full = True
                break
        if full:
            self.graph.cCount = len(self.graph.edgeList) # end
        else:
            rEdge = edges[r]
            rEdge.setColor(self.color)
            self.graph.incColor()
            
