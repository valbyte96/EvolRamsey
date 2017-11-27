from __future__ import absolute_import, division, print_function
'''---------------------------------Display.py----------------------------------------
@author: Ted McCulloch
This code is meant to be ran when a human wants to play against and AI (evolved
or not).
'''
'''---------------------------------IMPORTS----------------------------------------'''
import sys, os
from Graph import *
from DGraph import *
from Player import *
import random as rand
sys.path.append(os.path.abspath('../pyevolve'))
from graphics import *
import math
'''----------------------------------GLOBALS----------------------------------------'''

WIDTH = 500
HEIGHT = 500
n = 6
'''------------------------------------GAME----------------------------------------'''
def main():
    '''<---initialize graph and computer--->'''
    g = Graph(n)
    g.prep()
    win = GraphWin('Ramsey', WIDTH, HEIGHT)
    graph = DGraph(g, win, WIDTH/2, HEIGHT/2)
    graph.draw()
    comp = Player(1, g) # blue
    comp.setStrats(['build', 'block','build'])

    '''<---play the game--->'''
    while True:
        '''<---end + strategy switching checks--->'''
        if g.done(): #end
            print("done")
            break
        graph.check(comp)
        '''<---user's turn--->'''
        while True: # user's turn (TODO: TOGGLE WHO GOES FIRST)
            valid = False
            ans1, n1 = graph.isTouched(win.getMouse())
            if ans1: # first click
                while True:
                    ans2, n2 = graph.isTouched(win.getMouse())
                    if ans2 and n1.ID!=n2.ID: # second click
                        e = graph.getEdge(n1,n2)
                        if e!=False and not e.isColored():
                            # color the edge
                            e.drawEdge(win, 0)
                            g.incColor()
                            valid = True
                        else:
                            print("invalid edge")
                        break
                    else:
                        print("same node")
                        break
            if valid: # else redo user loop
                break
        '''<---end + strategy switching checks--->'''
        if g.done(): # end
            print("done")
            break
        graph.check(comp)
        '''<---computer's turn--->'''
        while True: # Computer's turn
            comp.play()
            break
        
    '''<---RESULT--->'''               
    print(g.winner()+" wins")
    
    '''<---close window--->'''
    win.getMouse()
    win.close()
    
    
    






main()
