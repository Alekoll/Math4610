#!/usr/bin/env python3

# g has to be a function that converges to a for f
def fixPoint(g,x0, tol, maxIter):
    i = 1
    error = 10 * tol

    while(error > tol and i < maxIter):
        i += 1
        x1 = g(x0)
        error = abs(x1 - x0)
        x0 = x1
    return x0

