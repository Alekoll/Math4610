#!/usr/bin/env python3

import cmath
# find the roots of a function in the form of aX^2 + bX + c = 0
# findRoots takes three parametes.

def findRoots(a,b,c):
    sqrt1 = (b**2) - (4*a*c)
    denom = 2*a
    negB = -b
    solutionList = []

    sol1 = (negB - cmath.sqrt(sqrt1))/denom

    sol2 = (negB + cmath.sqrt(sqrt1))/denom

    #solutionList[0] contains the negative value, and solutionList[1] contains the pos
    #value
    solutionList.append(sol1)
    solutionList.append(sol2)

    print(solutionList)
    return solutionList
findRoots(1,5,6)