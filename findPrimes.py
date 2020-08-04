#!/bin/python
import math
#import sys
#sys.setrecursionlimit(16894)
####  Previous line could be used to prevent overflow  ####

####  Returns a list up to the n-th prime  ####

pnum = []

def isPrime(test):
    i = 0
    while pnum[i] <= math.sqrt(test):
        if test%pnum[i] == 0:
            return False
        i += 1
    return True

def prime(n):
    for i in range(0,n):
        if i+1 <= len(pnum):
            p = pnum[i]
        if i == 0:
            p = 2
        elif i == 1:
            p = 3
        else:
            test = pnum[i-1]+2
            while not isPrime(test):
                test += 2
            p = test
        pnum.append(p)
    return pnum

print(prime(int(input())))
