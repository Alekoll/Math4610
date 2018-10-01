#!/usr/bin/env python3
import math
import fixPoint, bisection, newtonMethod, secant, hybridNewton, hybridSecant

def TestRootFinding():
    function1 = lambda x : x**2 - 3
    funciton1prime = lambda x: 2*x
    functionSin = lambda x :math.sin(math.pi * x)
    functionCos = lambda x : math.pi * math.cos(math.pi * x)

    tol = pow(10,-15)
    maxIter = 15

    fixPoint1 = fixPoint.fixPoint(lambda x: (x+3)/(x+1),2, tol,maxIter)

    bisection1 = bisection.bisection(function1, 1, 2, tol, maxIter)
    bisection2 = bisection.bisection(functionSin,.45, 1.45, tol, maxIter)

    newton1 = newtonMethod.NewtonMethod(function1, funciton1prime, 2, tol, maxIter)
    newton2 = newtonMethod.NewtonMethod(functionSin, functionCos, .45, tol, maxIter)

    secant1 = secant.Secant(function1, 1.5, 2, tol, maxIter)
    secant2 = secant.Secant(functionSin, .45, 1.45, tol, maxIter)

    hyNewton1 = hybridNewton.HybridNewton(function1, funciton1prime, 1, 3, tol, maxIter)
    hyNewton2 = hybridNewton.HybridNewton(functionSin, functionCos, 1, 1.5, tol, maxIter)

    hySecant1 = hybridSecant.hybridSecant(function1, 1, 2, tol, maxIter)
    hySecant2 = hybridSecant.hybridSecant(functionSin, 1, 1.5, tol, maxIter)

    print(fixPoint1, bisection1, bisection2, newton1, newton2, secant1, secant2, hyNewton1, hyNewton2, hySecant1, hySecant2, sep='\n')

TestRootFinding()

