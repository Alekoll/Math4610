#!/usr/bin/env python3

import cmath

def NewtonMethod(f, fPrime, x0, tol, maxIter):
    i = 1
    error = 10 * tol
    
    while (error > tol and i <= maxIter):
        i = i + 1
        x1 = x0 - f(x0)/fPrime(x0)
        error = abs(x1 - x0)
        x0 = x1
    if i == maxIter:
        print("I'm sorry, but there was not a root near by")
        return None
    else: 
        
        return x0
