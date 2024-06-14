#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#
from collections import Counter, defaultdict


def organizingContainers(container):
    # Write your code here
    container_capacity = {}

    balls_count_per_type = defaultdict(int)

    for i, con in enumerate(container):
        container_capacity[i] = sum(con)

    for i in range(len(container)):
        for j in range(len(container)):
            balls_count_per_type[i] += container[j][i]

    if sorted(balls_count_per_type.values())== sorted(container_capacity.values()):
        return "Possible"
    else:
        return "Impossible"
if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        #fptr.write(result + '\n')

   # fptr.close()
