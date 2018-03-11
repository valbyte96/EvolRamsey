'''StratSpaceTest.py
File takes a look at the strategy space for our five strategies over 5 intervals
this gives 5^5 or 3125 strategies to look over.
Idea'''

'''---------------------------------IMPORTS----------------------------------------'''
import sys, os
from Graph import *
from Player import *
from Chromosome import *
import random as rand
sys.path.append(os.path.abspath('../pyevolve'))
import cPickle as pickle
'''---------------------------------GLOBALS----------------------------------------'''
intervals = 5
chrome = ['build','block', 'adv-build', 'adv-block', 'random']
allStrats = Chromosome(['build','block','adv-build','adv-block','random'],intervals).getStrats() # all possible strategies
# IF YOU WANT PICKLED FIXED GRAPHS
filehandler = open('GraphList_n15_L3.obj', 'r') 
graphList = pickle.load(filehandler) # list of random graph objects
n = 15 # number of nodes
# incase fixed
fixed = True
#g = Graph(n)
g = graphList[0]
g.setInterval(intervals)
g.prep() # reset graph and prep triangles

'''---------------------------------FUNCTIONS----------------------------------------'''
def play(chromosome):
    '''this play function randomizes the graph every game'''
    
    if fixed:
        g.resetFixed()
    else:
        g.prep() # reset graph and prep triangles
    player1 = Player(0, g) # red
    player2 = Player(1, g) # blue
    player1.setStrats(chromosome) # set strat list as well as initial strategy
    player2.setStrats(allStrats[random.randint(0,len(allStrats)-1)])
    
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

    return g.winner()

def playN(chromosome):
    '''Play game n times in order to compare strategies'''
    nGames = 1000 # number of games to play
    p1Wins = 0
    p2Wins = 0
    ties = 0
    strats = []
    #for c in chromosome:
        #strats.append(chrome[int(c)])

    for i in range(nGames):
        win = play(chromosome)
        if win == "red":
            p1Wins+=1
        elif win == "blue":
            p2Wins+=1
        else:
            ties+=1
    return [p1Wins, p2Wins, ties, chromosome]

def main():
    result = []
    #C = [['1', '4', 4, 0, 3],[0, 0, 3, 2, 0],[0, 0, 3, 2, 0]]
    for c in allStrats:
        result.append(playN(c))
    print("done")
    result.sort(reverse=True)
    print(result[0:50]) # print top fifty
    

main()
