#!/usr/bin/env python3

#approximates the derivate of a function. It takes 3 inputs: h, and expression written as a lambda , value
def approxDeriv(h, f, a):
    return (f(a+h) - f(a))/h


