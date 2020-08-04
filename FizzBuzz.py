#!/bin/python

def fizzbuzz(upperLimit,fizz,buzz):
    i = 1
    while i <= upperLimit:
        printStatement = ''
        if i%fizz == 0:
            printStatement = 'fizz'
        if i%buzz == 0:
            printStatement += 'buzz'
        if printStatement == '':
            printStatement = str(i)
        print(printStatement)
        i = i+1
    return 0

print("Exit status:", fizzbuzz(int(input()),3,5))
