'''
CIS 313 Spring 2021 Assignment 5
Author: Thomas Joyce
Description: Takes a list of coin denominations and target values from stdin
             and writes the max number of coins which can be used to make the
             target value to stdout.
Date: 05/06/2021 -- Last Modified: 05/10/2021
Notes:
    1. if no file is specified when the program is run, it will prompt for user
       input. both file and user input should follow the format:
       int int #number of coin denominations #number of values
       int #coin denomination or value
       int #coin denomination or value
       ...
'''

#--------------------------------- Imports -------------------------------------

import sys
from math import inf

#-------------------------------------------------------------------------------
#-------------------------------- Functions ------------------------------------


def maxCoins(coins, value, memo):    
    '''
    Description: 
    Complexity: 
    Inputs: list[int], int
    Outputs: int
    '''
    for i in range(len(coins) + 1):
        for w in range(value + 1):
            if w < 0:
               memo[i][w] = -inf
            elif w > 0 and i == 0:
                memo[i][w] = -inf
            elif i == 0 or w == 0:
                memo[i][w] = 0
            elif coins[i-1] <= w:
                memo[i][w] = max(1 + memo[i-1][w-coins[i-1]], memo[i-1][w])
            else:
                memo[i][w] = memo[i-1][w]
    return memo


#---------------------------------- Main ---------------------------------------

def main():
    '''
    Description: 
    Inputs: file or user input
    Outputs:
    '''
    coins = []
    values = []
    contents = sys.stdin.readline()
    i, j = contents.strip().split()
    numCoins = int(i)
    numValues = int(j)
    for line in range(numCoins):
        coinTemp = [int(sys.stdin.readline())] * 5
        coins.extend(coinTemp)
    for line in range(numValues):
        values.append(int(sys.stdin.readline()))
    memo = [[0 for x in range(values[-1] + 1)] for x in range(len(coins) + 1)]
    memo = maxCoins(coins, values[-1], memo)
    for value in values:
        if memo[len(coins)][value] == -inf:
            print("target: {}, not possible".format(value))
        else:
            print("target: {}, max coins: {}".format(value, memo[len(coins)][value]))


if __name__ == '__main__':
    main()