
#!/bin/python3

import math
import os
# https://www.hackerrank.com/challenges/game-of-stones-1/problem?isFullScreen=true
#
# Complete the 'gameOfStones' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#
# in which case player  wins?
# when he makes the last move meaning n - move = 0 
# when he makes a move that puts n = 1
import random
import re
import sys


def gameOfStones(n):
    # Write your code here
    
    if n == 1:
        return 'First'

    if n % 7 in [0,1]:
        return 'Second'
    else:
        return 'First'




    


    
    






if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = gameOfStones(n)

        print(result)
