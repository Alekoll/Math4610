#!/usr/bin/env python3

import VectorOperations as op

def testVectorOp():

    x = [23,34,53]
    y = [12, 17, 7]

    additon = op.Addition(x,y)
    subtraction = op.Subtraction(x,y)
    innerProduct = op.InnerProduct(x,y)
    crossProduct = op.CrossProduct(x,y)
    scalarProduct = op.ScalarProduct(x, .5)

    print(additon, subtraction, innerProduct, crossProduct, scalarProduct, sep='\n')
testVectorOp()



