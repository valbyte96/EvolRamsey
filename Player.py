from __future__ import absolute_import, division, print_function
'''---------------------------------Player.py-----------------------------------
@author: Ted McCulloch
@version: 10/21/17
Class for implementing an iterative player, which will perform with
consistent strategies. 
'''
'''----------------------------------IMPORTS-----------------------------------'''
import sys, os
import random as rand
'''----------------------------------GLOBALS-----------------------------------'''
colorList = ["red", "blue"]
'''-----------------------------------CLASS------------------------------------'''
class Player:
    def __init__(self, ID, graph):
        self.ID = ID
        self.strat = "random" # default to random
        self.graph = graph
        self.color = colorList[ID]
        self.stratList = ["random"] # default to random
        self.display = False # assume no display
        
    def play(self):
        # TODO: if edges colored == 0 then do this else everything else
        if self.graph.cCount == 0:
            self.random() # TODO: come up with a self.first() strategy
        else:
            if self.strat == "block":
                self.block()
            elif self.strat == "build":
                self.build()
            elif self.strat == "random":
                self.random()
            else:
                if self.graph.verbose>-1: # TODO calibrate 
                    print("Warning: strategy doesn't exist")
                self.random()
            
    def setStrat(self, num):
        if num<len(self.stratList):
            self.strat = self.stratList[num]
        else:
            print("warning: id number greater than interval number")
            print("suggested index:",num)
            self.strat = self.stratList[0]

    def setStrats(self, strats):
        '''Responsible for initializing list of strategies as well as first strategy'''
        self.stratList = strats
        self.strat = strats[0]
    def onDisplay(self):
        '''call on non-user player if you want moves to display in gui'''
        self.display = True
        
    '''------------------------<<<STRATEGIES>>>-----------------------------------'''
    


    '''----------------------------------BUILD----------------------------------------'''
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
            if self.display:
                e.drawEdge(self.graph.win, self.ID)
            self.graph.incColor()
        else:
            # try another strategy
            if self.graph.verbose>0:
                print("build -> random")
            self.random()
    
    '''----------------------------------BLOCK----------------------------------------'''

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
            if self.display:
                e.drawEdge(self.graph.win, self.ID)
            self.graph.incColor()
        else:
            # try another strategy
            if self.graph.verbose>0:
                print("block -> build")
            self.build()
        
    '''----------------------------------RANDOM----------------------------------------'''
    def random(self):
        '''selects a random edge to color'''
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
            print("stopping condition")
            self.graph.cCount = len(self.graph.edgeList) # end
        else:
            rEdge = edges[r]
            rEdge.setColor(self.color)
            if self.display:
                rEdge.drawEdge(self.graph.win, self.ID)
            self.graph.incColor()
            
