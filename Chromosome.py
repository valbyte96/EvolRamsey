''' '''
from __future__ import absolute_import, division, print_function
import itertools

class Chromosome:
    def __init__(self, strats, intervals):
        self.intervals = intervals # num intervals
        self.strats = strats # list of strategies
        self.totalStrats = [p for p in itertools.product(strats, repeat=intervals)]
    def getStrats(self):
        return self.totalStrats
    def printC(self):
        print(self.totalStrats)

