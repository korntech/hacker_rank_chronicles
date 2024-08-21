#!/bin/python3

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#
import math
import os
import random
import re
import sys
from collections import deque


def is_prime(n):
    
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def waiter(number, q):

    prime_numbers = [] 
    start = 2
    while len(prime_numbers) < q:
        if is_prime(start):
            prime_numbers.append(start)

        start+=1 



    answers = []
    # Write your code here
    A = number 
    B = [] 
    for n in prime_numbers:

        len_A = len(A)
        tmp_B =  []
        tmp_A = []
        for i in range(len_A):
            popped = A.pop()
            if not popped % n:
                tmp_B.append(popped)
            else:
                tmp_A.append(popped)

        A = tmp_A
        answers.extend(reversed(tmp_B))

    if A:
        answers.extend(reversed(A))

    return answers

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    print(result)
