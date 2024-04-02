#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    sticks.sort(reverse=True)
    
    for i in range(0, len(sticks)):
        startSlice = i 
        endSlice = i + 3
        triplet = sticks[startSlice:endSlice]
        print(f"triplet is {triplet}")
        if len(triplet) < 3:
            break
       
        if (triplet[0] + triplet[1] > triplet[2]) and (triplet[0] + triplet[2] > triplet[1]) and (triplet[1] + triplet[2] > triplet[0]):
            triplet.sort()
            return triplet
    
    return [-1]
            

      #  print(f"start slice is {startSlice} and endslice is {endSlice}")
      #  print(f"the slice is {sticks[startSlice:endSlice]}")
    

    




if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    print(result)
