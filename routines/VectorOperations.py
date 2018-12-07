#!/usr/bin/env python3

#This file contains Vector Operations. Assuming that the vectos are the same size.

# create a new vector z where the elements ae the sum of x[i] + y[i]
def Addition(x,y):
    length = len(x)
    z = []

    for i in range(length):
        z.append(x[i] + y[i])

    return z

# create a new vector z where the elements ae the difference of x[i] - y[i]
def Subtraction(x,y):
    length = len(x)
    z = []

    for i in range(length):
        z.append(x[i] - y[i])

    return z

# multiple a scalar into the vector
def ScalarMultiplication(x, scalar):
    
    for i in range(len(x)):
        
        x[i] *= scalar    
    


# Return a float with the inner product of vectors x, y
def InnerProduct(x, y):
    
    length = len(x)
    z = 0.0

    for i in range (length):
        z += x[i] * y[i]
    
    return z

# Cross product of two vectors define in R3 X cross Y.
def CrossProduct(x, y):

    z1 = (x[1] * y[2]) - (x[2] * y[1])
    z2 = (x[2] * y[0]) - (x[0] * y[2])
    z3 = (x[0] * y[1]) - (x[1] * y[0])
    
    return [z1,z2,z3]
def Magnitude(v):
    x = 0
    for i in range(len(v)):
        x += v[i] * v[i]
    return (x**(.5))










