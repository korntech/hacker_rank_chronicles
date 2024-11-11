#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

    
def highestValuePalindrome(s, n, k):

    if k == 0:
        return s if s == s[::-1] else -1
    
    if n == 1:
        return '9' if k else -1
 
    mismatched =  0
    for i in range(n//2):
        if s[i] != s[-i-1]:
            mismatched += 1

    if mismatched > k:
        return '-1'
    
    s_list = ['' for _ in range(n)]
    
    for i in range(n//2):
        if s[i] != s[-i-1]:
            if s[i] == '9':
                s_list[-i-1] = '9'
                s_list[i] = '9'
                k -= 1
                mismatched -= 1
            elif s[-i-1] == '9':
                s_list[i] = '9'
                s_list[-i-1] = '9'
                k -=1
                mismatched -= 1
            else:
                if k - mismatched >= 1:
                    s_list[i] ='9'
                    s_list[-i-1] = '9'
                    k -= 2
                else:
                    bigger = max(int(s[i]), int(s[-i-1]))
                    s_list[i] = s_list[-i-1] = str(bigger)
                    k -= 1
                mismatched -= 1
        else:
            if k - mismatched >1 and s[i] != '9':
                s_list[i] = '9'
                s_list[-i-1] = '9'
                k -=2 
            else:
                s_list[i] = s[i]
                s_list[-i-1] = s[-i-1]
                
    
    if n % 2:
        if k > 0:
            s_list[n//2] = '9'
        else:
            s_list[n//2] = s[n//2]
    return ''.join(s_list)


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)
