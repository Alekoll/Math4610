#!/usr/bin/env python3

import bisection, secant

def hybridSecant(f, a, b, tol, maxIter):
    
    i = 0
    sec = None
    x = bisection.bisection(f, a, b, tol, 4)
    xa = x[0]
    xb = x[1]

    if(x is None):
        return None
    
    while (i < maxIter):
        
        i += 1
        
        sec = secant.Secant(f,xa, xb,tol,maxIter)

        if(sec is not None):
            return sec
        else:
            x = bisection.bisection(f, xa, xb, tol, 4)
            xa = x[0]
            xb = x[1]
        

