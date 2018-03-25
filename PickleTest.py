from __future__ import absolute_import, division, print_function
'''


'''
import cPickle as pickle
import time
import copy
filehandler = open('GraphList_n15_L5.obj', 'r') 
graphList = pickle.load(filehandler)

g = graphList[0]



def timer(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print(t2-t1)
        return t2-t1
    return wrapper
@timer
def method1():
    g.testMessage = "changed"
    g.resetFixed()
    return g
    

@timer
def method2():
    g_copy = copy.deepcopy(g)
    g.testMessage = "changed"
    return g_copy


def main():

    
    method1()
    
    method2()
    

main()
