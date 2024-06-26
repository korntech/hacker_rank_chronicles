#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    

    tmp_unsorted = []
    unsorted = []
    indexes_tmp = []
    indexes = []
    count = 0
    for i, v in enumerate(range(len(arr)-1)):
        if arr[i] > arr[i+1]:
            tmp_unsorted.append(arr[i])
            indexes_tmp.append(i)
        else:
            if tmp_unsorted:
                count += 1

                if count > 2:
                    print("no")
                    print("bla")
                    return
                indexes.extend(indexes_tmp)
                unsorted.extend(tmp_unsorted)
            tmp_unsorted = []
            indexes_tmp  = []

    if tmp_unsorted:
        unsorted.extend(tmp_unsorted)
    if indexes_tmp:
        indexes.extend(indexes_tmp)



    if len(unsorted) <= 2:
     
        zipped = list(zip(unsorted, indexes))
        # swap only possible 
        # two situations where values are smaller so swap only possible in not adjacent indexes
        if len(unsorted) == 2:
         #   print(zipped)
            l_ind = zipped[0][1]
            # we swap one number ahead which is smaller  - the only chance for success
            u_ind = zipped[1][1] + 1
            arr_cp = arr[:]
            arr_cp[l_ind], arr_cp[u_ind] = arr_cp[u_ind], arr_cp[l_ind]

            if arr_cp == sorted(arr):
                print("yes")
                print(f"swap {l_ind+1} {u_ind+1}")
                return
        else:
            arr_cp = arr[:]
            i = indexes[0]
            arr_cp[i], arr_cp[i+1] = arr_cp[i+1], arr_cp[i]

            if sorted(arr) == arr_cp:
                print("yes")
                # need to account for 1-based indexing
                print(f"swap {i+1} {i+1+1}")
                return
    else:
        arr_cp = arr[:]
        start_range = indexes[0]
        # we add 2 to account for the next smaller number and not inclusive range
        end_range = indexes[-1] + 2
        arr_cp[start_range:end_range] = sorted(arr[start_range:end_range])
        if arr_cp == sorted(arr):
            print("yes")
            print(f"reverse {start_range+1} {end_range}")
            return
        else:
            print("no")
            return
    print("no")



    
    
            


                
            


if __name__ == '__main__':
  #  n = int(input().strip())

   # arr = list(map(int, input().rstrip().split()))
    with open("sorted.txt", "r") as f:
        text = f.read().split(" ")




    almostSorted(text)
