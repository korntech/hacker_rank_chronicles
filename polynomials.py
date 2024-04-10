import numpy

coefs = list(map(numpy.float64, input().split()))
x = int(input())
print(numpy.polyval(coefs,x))