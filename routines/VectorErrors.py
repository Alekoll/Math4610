#!/usr/bin/env python3

import lengthnorms, relError, absError

# 6 functions to compute the absolute error and the relative error of two vectors where vector Y is the exact Vectur

def AbsErrorLengthNorm1(vectorX, vectorY):
    lengthX = lengthnorms.LengthNorm1(vectorX)
    lengthY = lengthnorms.LengthNorm1(vectorY)

    return absError.absError(lengthX, lengthY)

def RelErrorLengthNorm1(vectorX, vectorY):
    lengthX = lengthnorms.LengthNorm1(vectorX)
    lengthY = lengthnorms.LengthNorm1(vectorY)

    return relError.relError(lengthX, lengthY)

def AbsErrorLengthNorm2(vectorX, vectorY):
    lengthX = lengthnorms.LengthNorm2(vectorX)
    lengthY = lengthnorms.LengthNorm2(vectorY)

    return absError.absError(lengthX, lengthY)

def RelErrorLengthNorm2(vectorX, vectorY):
    lengthX = lengthnorms.LengthNorm2(vectorX)
    lengthY = lengthnorms.LengthNorm2(vectorY)

    return relError.relError(lengthX, lengthY)

def AbsErrorLengthNormInf(vectorX, vectorY):
    lengthX = lengthnorms.LengthNormInf(vectorX)
    lengthY = lengthnorms.LengthNormInf(vectorY)

    return absError.absError(lengthX, lengthY)
    
def RelErrorLengthNormInf(vectorX, vectorY):
    lengthX = lengthnorms.LengthNormInf(vectorX)
    lengthY = lengthnorms.LengthNormInf(vectorY)

    return relError.relError(lengthX, lengthY)