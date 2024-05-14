#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/an-interesting-game-1/problem?isFullScreen=true
#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def gamingArray(arr):
    # Write your code here
    # counter number of deletions 

    my_dict = {v: k for k,v in dict(enumerate(arr)).items()}

    my_dict = dict(sorted(my_dict.items(), reverse=True))

    print(my_dict)
    counter = 1
    _, current_val = next(iter(my_dict.items()))
    for key,val in my_dict.items():
        if val < current_val:
            current_val = val
            counter += 1

    if counter % 2:
        return 'BOB'

    else:
        return 'ANDY'
        
        


    





    

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        print(result)

       # fptr.write(result + '\n')

   # fptr.close()
