#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#
def find_pat(line, P, current_pat):
    tmp = []
    start = 0
    while start < len(line):
            start = line.find(P[current_pat], start)
            if start == -1:
                break
            tmp.append(start)
            start += 1
    return tmp

def gridSearch(G, P):
    # Write your code here
    current_pat = 0
    table = {}
    for i, line in enumerate(G):

        tmp = find_pat(line, P, current_pat)      
        if tmp:    
            table[current_pat] = tmp
            current_pat += 1
            if len(table) >1:
                if (current_pat-1 in table) and (current_pat-2 in table) and set(table[current_pat-1]) & set(table[current_pat-2]):
                    if current_pat  == len(P):
                        #print(table)
                        return "YES"
                    continue
                else:   
                    if P[0] in line:
                        tmp = find_pat(line, P, 0)
                        table[0] = tmp
                        if tmp:
                            current_pat = 1
                        else:
                            current_pat = 0
                    else:
                        current_pat = 0
        else:
            if P[0] in line:
                tmp = find_pat(line, P, 0)
                table[0] = tmp
                if tmp:
                    current_pat = 1
                else:
                    current_pat = 0
            else:
                current_pat = 0


                    
        
    
            
            

        if current_pat  == len(P):
            #print(table)
            return "YES"
       
        
               
        


    return "NO"


    print(f"P is {P}")
if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)
        print(result)
      #  fptr.write(result + '\n')

   # fptr.close()
