#!/usr/bin/env python3
from Gauss_Elim import Upper as Upper
from MatrixOperations import Trace as Trace
import copy

#The outer product of two matrices

#The Kronecker product of two matrices

#Finds the determinant of Matrix A by finding the upper triangle matrix then mutiplying the diagonal together.
def Det(A):
    B = copy.deepcopy(A)
    deter = 0.0
    n = len(A[0])
    Upper(B,([0]*n))
    deter = Trace(B)
    return deter