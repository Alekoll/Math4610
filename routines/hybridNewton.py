#!/usr/bin/env python3

import bisection, newtonMethod

def HybridNewton (f, fprime, a, b, tol, maxIter):

    error = 10 * tol
    i = 0
    newton = None

    
    x = bisection.bisection(f, a, b, tol, 4)
    xa = x[0]
    xb = x[1]

    if(x is None):
        return None
    
    while (i < maxIter):

        i += 1
        x0 = .5*(xa + xb)
        
        newton = newtonMethod.NewtonMethod(f,fprime, x0, tol, maxIter)

        if(newton is not None):
            print(i)
            return newton
        else:
            x = bisection.bisection(f, xa, xb, tol, 4)
            xa = x[0]
            xb = x[1]
        
    print(i)
    return newton
        
print(HybridNewton(lambda x: x**2 - 3, lambda x: 2*x,-100,-1, pow(10, -15), 15))