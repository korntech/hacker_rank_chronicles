#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    ind = 1
    count = 0
    for char in s:
        if ind == 1 and char != 'S':
            count += 1
        elif ind == 2 and char != 'O':
            count += 1
        elif ind == 3 and char != 'S':
            count += 1
        if ind == 3:
            ind = 1
        else:
            ind += 1

  
    
 
       

        
        
            
    return count
    



if __name__ == '__main__':

    s = input()

    result = marsExploration(s)

    print(result)
