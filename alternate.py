#!/bin/python3
#https://www.hackerrank.com/challenges/two-characters/problem?isFullScreen=true
import math
import os
import random
import re
import sys
#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
import time


def alternate(s):
    if len(s) == len(set(s)) and len(s) != 1:
        return len(s)
    if len(s) == 1:
        return 0
    
    unique = list(set(s))
    
    combs = [(unique[i], unique[j]) for i in range(len(unique)) for j in range(i+1, len(unique))]

    cands = []
    for comb in combs:
        new_s = [char for char in s if char in comb]
        for i in range(len(new_s)-1):
            if new_s[i] == new_s[i+1]:
                break
        else:
            if len(new_s) >= 4:
               cands.append(new_s)
    

    return max(map(lambda x: len(x), cands)) if cands else 0


   
   



if __name__ == '__main__':
 #   fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)
    print(result)
    


