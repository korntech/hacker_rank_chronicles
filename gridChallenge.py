#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#
# https://www.hackerrank.com/challenges/grid-challenge/problem?isFullScreen=true

def gridChallenge(grid):
    # Write your code here
    col_length = len(grid[0])
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])


    for j in range(col_length):
        for i in range(len(grid) - 1):
            if ord(grid[i][j]) > ord(grid[i+1][j]):
                 return 'NO'
    
    return 'YES'







if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)
        print(result)
        
