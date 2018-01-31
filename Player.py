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
            s = self.strat
            if s == "block" or s == "build" or s == "adv-build" or s == "adv-block":
                self.move()
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
    '''----------------------------------MOVE----------------------------------------'''
    
    def move(self):
        edges = self.graph.edgeList
        hScore = 0 # high score
        score = 0 # necessary?
        sEdge = None # saved edge
        '''loop through all edges'''
        for e in edges:
            if e.notColored == 0:
                continue
            if self.strat == 'build':
                score = e.getScoreBuild(self.color)
            elif self.strat == 'block':
                score = e.getScoreBlock(self.color)
            elif self.strat == 'adv-build':
                score = e.getScoreAdvBuild(self.color)
            elif self.strat == 'adv-block':
                score = e.getScoreAdvBlock(self.color)
            if score>hScore:
                hScore = score
                sEdge = e
        if sEdge!=None:
            sEdge.setColor(self.color)
            if self.display:
                sEdge.drawEdge(self.graph.win, self.ID)
            self.graph.incColor()
                
        else:
            # if all edges are same choose one at random
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
            
