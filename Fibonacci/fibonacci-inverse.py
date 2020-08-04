#!/bin/python
from fibonacci import fib

n = int(input())
i = 0
while fib(i) <= n:
    if fib(i) == n:
        print(i)
        break
    i += 1
if fib(i) > n:
    print('-1')
