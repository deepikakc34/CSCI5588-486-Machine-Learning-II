import numpy as np
import os
import collections
from math import exp


class SimulatedAnnealing:
    """ 
    Initializing the constants 
    STRING_LENGTH and NUMBER_OF_ITERATIONS 
    """
    def __init__(self):
        self.STRING_LENGTH = 50
        self.MAX = 200
    
    """ 
    The below function creates a random array of 0's and 1's
    given the array size and how many ones you want in that array   
    """
    def CreateRandomArray(self,arsize,ones):
        A = np.ones(ones, dtype=np.int)
        B = np.zeros(arsize-ones, dtype=np.int)
        C = np.concatenate((A, B), axis = 0)
        # print(C)
        np.random.shuffle(C)
        return C
    
    """ 
    The below function calculates the fitness value for the given random array
    It counts the number of 1's in the given array and applies that in the function and returns
    the fitness value 
    """
    def CalculateFitness(self,onescount):
        return abs(14*onescount-190)

    def getOnesCount(self,arr):
        return collections.Counter(arr)[1]
    
    """ 
    Given an array of length asize this function returns a array list of 
    one bit changed neighbours of length asize 
    """
    def getNeighbours(self,arr,asize): 
        neighbours = []
        for index in range(asize):
            temparr = list(arr)
            temparr[index] = 1 - arr[index]
            neighbours.append(temparr)
        return neighbours
    
    """ 
    Given a array list of arrays 
    this function returns calculates Fitness value for each array in the list and 
    returns the largest fitness value 
    """
    def GetLargestFV(self,arr):
        largestFV = 0
        for a in arr:
            currentOnesCount = self.getOnesCount(a)
            currentFV = self.CalculateFitness(currentOnesCount)
            if currentFV > largestFV:
                largestFV = currentFV
                largestVN = a
        return largestVN

def main():
    sa = SimulatedAnnealing()

    #reset the algorithm for MAX times
    t = 0
    Temperature = 100
    randomVC = sa.CreateRandomArray(sa.STRING_LENGTH,np.random.randint(0,sa.STRING_LENGTH))
    """
    Calculating the number of ones for the random VC and Evaluating the fitness value 
    for VC
    """
    randomOnescount = sa.getOnesCount(randomVC)
    functionvalueRandomVC = sa.CalculateFitness(randomOnescount)

    while t < sa.MAX:
        neighbours = sa.getNeighbours(randomVC,sa.STRING_LENGTH)
        for neighbour in neighbours:
            onescount = sa.getOnesCount(neighbour)
            functionValuelargestVN = sa.CalculateFitness(onescount)
            expcalc = exp((functionValuelargestVN - functionvalueRandomVC)/Temperature)
            if functionvalueRandomVC < functionValuelargestVN:
                functionvalueRandomVC = functionValuelargestVN
                randomVC = neighbour
            elif np.random.uniform(0,1)< expcalc:
                functionvalueRandomVC = functionValuelargestVN
                randomVC = neighbour
            
        if t < (sa.MAX-1):
            print(functionvalueRandomVC,end='')
            print(',',end='')
        else:
            print(functionvalueRandomVC)
        
        Temperature = Temperature * 0.95
        t += 1
if __name__=="__main__":
    main()
