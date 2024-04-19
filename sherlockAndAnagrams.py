#!/bin/python3

import math
import os
import random
import re
import sys
# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?isFullScreen=true
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
from collections import defaultdict
from math import factorial


def combinations(n, k):

    return factorial(n) // (factorial(k) * factorial(n-k))


def sherlockAndAnagrams(s):
    # Write your code here
    
    count = defaultdict(int)

    for char in s:
        count[char] += 1
    
    if all(list(map(lambda x: x==1, list(count.values())))):
        return 0
    count = defaultdict(int)
    for i in range(1, len(s)):
        tmp = []
        print(f"i is {i}")
        startSlice = 0 
        endSlice = i 
        for char in s:
            count[''.join(sorted(s[startSlice:endSlice]))] +=1
            startSlice += 1
            endSlice += 1

            if endSlice > len(s):
                break
 
    count_sum =  {k: combinations(v, 2) for k,v in count.items() if v >= 2}


    return sum(count_sum.values())





    
    


if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)
        print(result)

        #fptr.write(str(result) + '\n')

   # fptr.close()
