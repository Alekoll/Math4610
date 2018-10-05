#!/usr/bin/env python3

#This file contains the l1, l2, and linf routines

#compute the l1. input: a vector in a for as a list. return a float of the sum of all the elements in the vector
def LengthNorm1(vector):
    
    length1 = 0.0

    for element in vector:
        length1 += abs(element)

    return length1

#compute the l2. input: a vecotr as a list
def LengthNorm2(vector):
    
    length2 = 0.0

    for element in vector:
        length2 += abs(element)**2
    
    return length2**(1/2)

#compute linf. input: vector as a list

def LengthNormInf(vector):

    lengthInf = max(vector)

    return float(lengthInf)





    