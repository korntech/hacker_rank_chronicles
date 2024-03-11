
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    cities_with_space_stations = c
    cities = sorted(cities_with_space_stations)
    mins = []
   

    without_space_stations = set(range(n)) - set(cities_with_space_stations)

  
    for target in without_space_stations:
        tmp = []
        low, high = 0, len(cities) - 1
        while low <= high:

            mid = (low+high) // 2
            if cities[mid] < target:
                low = mid + 1
                best_match = cities[mid]
            else:
                high = mid - 1
                best_match = cities[mid] 
            
            tmp.append(abs(target-best_match))
        mins.append(min(tmp))
    

    return max(mins)

if __name__ == '__main__':
  #  fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    print(result)