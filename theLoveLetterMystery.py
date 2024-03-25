#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/the-love-letter-mystery/problem?isFullScreen=true
#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    
    count_a = 0
    count_b = 0
    if s == s[::-1]:
        return 0 

    # handle odds strings
    if len(s) % 2:
        first_part = s[:len(s)//2]
        second_part = s[len(s)//2+1:]
    else:
        first_part = s[:len(s)//2]
        second_part = s[len(s)//2:]

    for pair in zip(first_part, reversed(second_part)):
        
        if pair[0] != pair[1]:
            count_a += abs(ord(pair[0]) - ord(pair[1]))


    for pair in zip(second_part, reversed(first_part)):
        if pair[0] != pair[1]:
            count_b += abs(ord(pair[0]) - ord(pair[1]))       




    return min(count_b, count_a)


if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        print(result)
