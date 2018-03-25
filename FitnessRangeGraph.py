from __future__ import absolute_import, division, print_function
'''FitnessRangeGraph.py
The idea behind this program is to take in a number of strategies, play n games
on each of strategy t times, graph the mean fitness as well as itermediate points 

Point is to see variation 

'''
import matplotlib.pyplot as plt
import numpy as np
'''---------------------------------IMPORTS----------------------------------------'''
import sys, os
from Graph import *
from Player import *
from Chromosome import *
import random as rand
sys.path.append(os.path.abspath('../pyevolve'))
from pyevolve import *
import cPickle as pickle
'''----------------------------------GLOBALS----------------------------------------'''
intervals = 5 # number of game intervals
n = 15 # number of nodes
chrome = ['build','block', 'adv-build', 'adv-block', 'random']
p2Chrome = Chromosome(['build','block', 'adv-build', 'adv-block', 'random'],intervals).getStrats() # all possible chromosomes

# IF YOU WANT PICKLED FIXED GRAPHS
filehandler = open('GraphList_n15_L1000.obj', 'r') 
graphList = pickle.load(filehandler) # list of random graph objects
# incase fixed
fixed = True
#g = Graph(n)
#g = graphList[1]
#g.setInterval(intervals)
#g.prep() # reset graph and prep triangles

'''----------------------------------PLAY----------------------------------------'''



def play(chromosome):
    '''this play function randomizes the graph every game'''
    
    #if fixed:
        #g.resetFixed()
    g = graphList[rand.randint(0,999)]
    g.setInterval(intervals)
    # reset graph and prep triangles
    player1 = Player(0, g) # red
    player2 = Player(1, g) # blue
    
    player1.setStrats(chromosome) # set strat list as well as initial strategy
    player2.setStrats(p2Chrome[random.randint(0,len(p2Chrome)-1)])
    
    r = 0 # debug
    unit = g.getNumEdges()/intervals

    # randomizes who goes first
    first = rand.randint(0,1)
    
    
    while(True):
        if first==0: # player 1 goes first
            if g.done(): # stop
                break
            player1.play()
            g.checkInterval(player1, player2)
                
            if g.done(): # stop
                break

            player2.play()
            g.checkInterval(player1, player2)
            r+=1 # debug

        else: # player 2 goes first
            if g.done(): # stop
                break
            player2.play()
            g.checkInterval(player1, player2)
                
            if g.done(): # stop
                break

            player1.play()
            g.checkInterval(player1, player2)
            r+=1 # debug
    winner = g.winner()
    g.resetFixed()
    return winner



def playN(chromosome, nGames):
    '''Play game n times in order to compare strategies'''
    p1Wins = 0
    p2Wins = 0
    ties = 0
    strats = []
    for c in chromosome:
        strats.append(chrome[int(c)])

    for i in range(nGames):
        win = play(strats)
        if win == "red":
            p1Wins+=1
        elif win == "blue":
            p2Wins+=1
        else:
            ties+=1
    #return [p1Wins, p2Wins, ties]
    return [p1Wins]

def mean(L):
    s = 0
    for i in L:
        s+=i[0]
    return s/len(L)
def parse(results):
    means = []
    for stratL in results:
        means.append(mean(stratL))
    return means
        

def tmain():

    s = [[[10, 0, 0], [8, 2, 0], [9, 1, 0], [9, 0, 1], [7, 3, 0]],
         [[8, 2, 0], [10, 0, 0], [7, 3, 0], [8, 1, 1], [10, 0, 0]],
         [[7, 3, 0], [7, 2, 1], [7, 2, 1], [6, 4, 0], [9, 1, 0]],
         [[8, 1, 1], [8, 2, 0], [7, 2, 1], [7, 2, 1], [8, 2, 0]],
         [[8, 2, 0], [3, 7, 0], [7, 2, 1], [8, 2, 0], [6, 4, 0]],
         [[9, 1, 0], [9, 1, 0], [8, 1, 1], [9, 1, 0], [9, 1, 0]]]
    
    graph(s, 10)


def graph(results, n):
    means = parse(results)
    sLen = len(means)
    x = [i+1 for i in range(sLen)]

    objects = ["Strat"+str(i) for i in range(sLen)]
    plt.xticks(x, objects, rotation='horizontal')
    # plot means
    plt.plot([x], [means], marker='o', markersize=7, color="red")
    # plot results range
    for i in range(sLen):
        for j in results[i]:
            plt.plot(i+1,j[0],marker='x', markersize=3, color="blue")

    # adjust axis
    plt.ylim(ymax=n+1) 
    plt.ylim(ymin=0)
    plt.xlim(xmin=.5)
    plt.xlim(xmax=sLen+.5)
    plt.show()

    
    



def main():
    s = 20 # sample size
    n = 1000 # number of games per sample
    # top 6 strategies
    #strats = [[2, 0, 2, 2, 4], [2, 2, 2, 2, 4], [2, 1, 2, 2, 4],
              #[2, 3, 0, 2, 4], [3, 0, 2, 2, 4], [3, 2, 2, 2, 4]]
    strats = input("input strats: ")
    

    stratResults = []
    for strat in strats:
        results = []
        for i in range(s):
            results.append(playN(strat, n))
        stratResults.append(results)
    graph(stratResults, n)


    
            
            
            
        

    



main()
