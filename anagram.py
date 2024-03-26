#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# https://www.hackerrank.com/challenges/anagram/problem?isFullScreen=true

def anagram(s):
    # Write your code here
    if len(s) % 2:
        return -1
    ops = 0
    first_part = s[:len(s)//2]
    second_part = s[len(s)//2:]
    
    for char in set(second_part):
        char_1_count = second_part.count(char)
        char_2_count = first_part.count(char)

        diff = abs(second_part.count(char) - first_part.count(char))

        if char_1_count > char_2_count:
            ops += diff
            
        

        
    return ops

if __name__ == '__main__':
  #  fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        print(result)
