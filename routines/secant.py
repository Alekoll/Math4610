#!/usr/bin/env python3


def Secant(f, x0, x1, tol, maxIter):

    i = 0
    error = 10 * tol

    while(error > tol and i < maxIter):

        i = i + 1
        x2 = x1 - (f(x1)*(x1 - x0))/(f(x1) - f(x0))
        error = abs(x2-x1)
        x0 = x1
        x1 = x2

    return x0



