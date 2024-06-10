#!/bin/python3

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#
import math
import os
import random
import re
import sys


def counterGame(n):
    # Write your code here
    
    table = {}
    for i in range(64, 0, -1):

        table[2**i] = i 

    
    if n in table:
        c = table[n]
    else:
        c = 0 
        while n != 1:
            for key, _ in table.items():
                if n > key:
                    n -= key
                    c += 1
            if n in table:
                c += table[n]
                break

    
    
    if c % 2:
        return "Louise"
    else:
        return "Richard"
    
    

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)
        print(result)
        #fptr.write(result + '\n')

  #  fptr.close()
