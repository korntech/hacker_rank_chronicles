import numpy

arr = []
N = int(input())

for i in range(N):
    arr.append(list(map(numpy.float64, input().split())))
    
print(round(numpy.linalg.det(arr), 2))