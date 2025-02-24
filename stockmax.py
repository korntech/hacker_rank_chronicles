#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    max_val = 0 
    profit = 0 
    for i in range(len(prices)-1, -1, -1):
        max_val = max(prices[i], max_val)
        
        if max_val > prices[i]:
            profit += max_val - prices[i]


    return profit





            
       

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

     #   fptr.write(str(result) + '\n')

    print(result)

   # fptr.close()
