#!/usr/bin/env python3

from VectorOperations import ScalarMultiplication as scalar

# Suppose A and B are matrices of the n x n, A + B = C is the C[i][j] = A[i][j] + B[i][j]
def Addition(A, B):
    row = len(A)
    col = row
    C = [[0]* row for _ in range(row)]
    for i in range(row):
        for j in range(col):
            C[i][j] = A[i][j] + B[i][j]
    return C
    

# Suppose A and B are matrices of the n x n, A - B = C is the C[i][j] = A[i][j] - B[i][j] s

def Subtraction(A, B):
    row = len(A)
    col = row

    C = [[0]* row for _ in range(row)]

    for i in range(row):
        for j in range(col):
            C[i][j] = A[i][j] - B[i][j]
    return C

# T(A) is a new matrix where the columns and rows are swapped
def Transpose(A):
    row = len(A)
    col = len(A[0])
    #creating an empty list
    transpose = []
    for j in range (col):
        rows = []
        for i in range (row):
            element = A[i][j]
            rows.append(element)
        transpose.append(rows)

    return transpose
#Trace(A) is the sum of the main diagonal of an nxn matrix
def Trace(A):
    row = len(A[0])
    trace = 0.0
    for i in range(row):
        trace += A[i][i]
    return trace

def Scalar(A, alpha):
    row = len(A)
    col = len(A[0])

    for i in range(row):
        for j in range(col):
            A[i][j] *= alpha

# A is the matrix, and x is the vector. given n x m matrix,  n X 1 vector, find the product
def VectorMatrixMultiplication(A, x):
    row = len(A)
    col = len(A[0])
    product = [0]*row
    for j in range(col):
        rows = []
        for i in range(row):
            rows.append(A[i][j])
        
        scalar(rows, x[j])
        for i in range(row):
            product[i] += rows[i]
        
    return product
# A = m x n, B = n x p, c = m x p
def MatrixMultiplication(A,B):
    row = len(A)
    col = len(B[0])
    m = len(A[0])
    
    C = [[0] * row for i in range(col)]
    
    for i in range(row):
        for j in range(col):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    
    return C
#given a matrix, reduce the rows
A = [[1,2,3],[5,7,11],[13,17,19]]
B = [[1,2,3],[4,5,6],[7,8,9]]
C = MatrixMultiplication(A,B)

