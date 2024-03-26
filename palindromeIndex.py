#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/palindrome-index/problem?isFullScreen=true
#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here

    if s == s[::-1]:
        return -1
    s_length = len(s)
    for i in range(s_length // 2):
        if s[i] != s[s_length-i-1]:
            # now we will take some action 
            
            if s[:i] + s[i+1:] == (s[:i] + s[i+1:])[::-1]:
                return i 
        
            if s[:len(s)-i-1] + s[len(s)-i:] == (s[:len(s)-i-1] + s[len(s)-i:])[::-1]:
                return len(s) - i - 1
            else:
                return -1 



            
            


    
        

    

    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        print(result)