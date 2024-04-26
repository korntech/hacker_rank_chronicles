#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#
# https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true
def biggerIsGreater(w):
    # Write your code here

    w = list(w)
    if len(set(w)) == 1 or list(w) == sorted(w)[::-1]:
        return 'no answer'
    else:
        reversed_w  = list(reversed(w))
        for i in range(len(w)-1):
            if reversed_w[i] > reversed_w[i+1]:
                for ind, char in enumerate(sorted(reversed_w[:i+1])):
                    if char > reversed_w[i+1]:
                        winner = char
                        break
                reversed_w[ind], reversed_w[i+1] = reversed_w[i+1], winner
                reversed_w[:i+1] = reversed(sorted(reversed_w[:i+1]))
                return ''.join(reversed_w[::-1])
                    

                
                



                

            


        




if __name__ == '__main__':
  #
    T = int(input().strip())
    wyniki = []

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)
        wyniki.append(result)

        print(f"Wyniki are like this:------")
        print(*wyniki, sep="\n")