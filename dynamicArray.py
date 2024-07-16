#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    
    lastAnswer = 0 

    arr = [[] for _ in range(n)]
    answers = []
    for query in queries:
        idx = (query[1] ^ lastAnswer) % n 
        if query[0] == 1:
            
            answers.append(arr[idx].append(query[2]))
        else:
            lastAnswer = arr[idx][query[2] % len(arr[idx])]
            answers.append(lastAnswer)

    return [x for x in answers if x]
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print(result)
