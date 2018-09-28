#!/usr/bin/env python3
# 
import math

def bisection(f, a, b, tol, maxIter):
    #initalize the f(a) and (b) and the k value
    fa = f(a)
    fb = f(b)
    k = int(math.log2(tol/abs(b-a))/math.log2(1/2) + 1)
    
    if (maxIter == 4):
        k = maxIter
    
    # Check if the given interval contains the root
    if(fa * fb < 0.0):

        for i in range (0, k):
            c = .5*(a+b)
            fc = f(c)
            if(fa*fc < 0):
                b = c
                fb = fc
            else:
                a = c
                fa = fc
        
        return a,b
    else:
        print("Sorry, but this interval does not contain a root")
        return None 
