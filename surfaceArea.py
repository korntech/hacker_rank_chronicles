#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A, H, W):
    # Write your code here

    surface = 0 

    if H == 1 or W == 1:
        if H > W:
            for i in range(H-1):
                if i == 0:
                    surface += A[i][0]
                surface += abs(A[i][0]-A[i+1][0])
                surface += A[i][0] * 2
            surface += A[i+1][0]
            surface += (H*W) * 2
            surface += A[i+1][0] * 2

        elif H < W:
            for i in range(W-1):
                if i == 0:
                    surface += A[0][i]
                surface += abs(A[0][i]-A[0][i+1])
            surface += A[0][i+1]
            surface += sum(map(lambda x: 2*x, A[0]))
            surface += (H*W) * 2
        else:
            surface += 4 * A[0][0] + 2

        return surface
                

            

  #  print(A)
    for i in range(H):
        for j in range(W-1):
            # front side
            if j == 0:
                surface += A[i][j]
            try:
                surface += abs(A[i][j]-A[i][j+1])
            except IndexError:
                print(f"j is {j} and i is {i}")
    
        surface += A[i][j+1]  



    for i in range(W):
        for j in range(H-1):
            # front side
            if j == 0:
                surface += A[j][i]
            try:
                surface += abs(A[j][i]-A[j+1][i])
            except IndexError:
                print(f"j is {j} and i is {i}")
                print(f"j+1 is {j+1}")

        surface += A[j+1][i]

    # add tops and bottoms 
    surface += (H*W) * 2

    
    return surface

    
if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A, H, W)

    print(result)

   # fptr.write(str(result) + '\n')

  #  fptr.close()
