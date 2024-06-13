#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#
# let'ss reverse columns :) 
def flippingMatrix(matrix, n):

    max_total = 0


    for i in range(n):
        for j in range(n):


            max_val = max(matrix[i][j], 
                          matrix[i][2*n-1-j],
                          matrix[2*n-1-i][j],
                          matrix[2*n-1-i][2*n-1-j])

    
            max_total += max_val
            print(max_val)

    print(max_total)


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix, n)

        

        print(result)
