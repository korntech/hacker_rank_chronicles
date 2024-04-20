#!/bin/python3

import math
import os
import random
import re
import sys


# n- number of flowers
# k - number of customers
# Complete the getMinimumCost function below.
def getMinimumCost(n, k, c):

    if k >= n:
        return sum(c)
    else:
        min_cost = 0 
        c = sorted(c)
        bought_flowers = n - k 
        min_cost += sum(c[bought_flowers:])
        left_flowers = sorted(c[:bought_flowers], reverse=True)

        factor = 2 
        k_tracker = 0 
        for flower in left_flowers:

            min_cost += factor * flower 
            k_tracker += 1
            if k_tracker == k:
                k_tracker = 0 
                factor +=1 
        
    
       
     
        return min_cost


            







        








if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(n, k, c)

    print(minimumCost)
