'''Display.py
@author: Ted McCulloch
'''

from __future__ import absolute_import, division, print_function
import sys, os
from Graph import *
from DGraph import *
from Player import *
import random as rand
sys.path.append(os.path.abspath('../pyevolve'))
#from pyevolve import *
from graphics import *
import math

WIDTH = 500
HEIGHT = 500
n = 6


def main():
    g = Graph(n)
    g.prep()
    win = GraphWin('Ramsey', WIDTH, HEIGHT)
    graph = DGraph(g, win, WIDTH/2, HEIGHT/2)
    graph.draw()

    comp = Player(1, g) # blue
    comp.setStrats(['build', 'block'])

    # GAME LOOP
    while True:
        while True: # user's turn (TODO: TOGGLE WHO GOES FIRST)
            #TODO: double click same node bug
            print("user turn")
            valid = False
            ans1, n1 = graph.isTouched(win.getMouse())
            if ans1: # first click
                while True:
                    ans2, n2 = graph.isTouched(win.getMouse())
                    if ans2: # second click
                        e = graph.getEdge(n1,n2)
                        if e!=False and not e.isColored():
                            # color the edge
                            e.drawEdge(win, 0)
                            valid = True
                        else:
                            print("invalid edge")
                        break
            if valid: # else redo user loop
                break
        print("computer turn")
        while True: # Computer's turn
            #n1, n2 = graph.getRand() # get two available nodes
            #e = graph.getEdge(n1,n2)
            #graph.drawEdge(e,1)
            comp.play()
            break
            

    # close window 
    win.getMouse()
    win.close()
    
    
    






main()
