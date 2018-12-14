import random
import math
import MatrixOperations
import copy
import time
import VectorOperations
#homework set 4
#Gauss-Elimination without setting the values below the pivots to zero. Also, for a squared matrix
def Upper(A,b):
    n = len(A[0])
    m = len(A)

    for k in range(n-1):
        for i in range(k+1, m):
            factor = A[i][k]/A[k][k]
            A[i][k] = -factor
            for j in range(k+1, n):
                A[i][j] = A[i][j] -(factor*A[k][j])
            b[i] -= factor*b[k]
#performs Gauss-Elimination, then returns the lower triangle matrix with 1 in the diagonal


# Guass-Elimination that returns a list of the multiples used. first use guassian elimination, then forward sub, then backward sub
def LUDecomposition(A,b):
   
    #perform Guassian Elimination where it modifies to a  upper and lower triangular matrix
    Upper(A,b)
    #Forward Substitution is performed on the modified Matrix, and produces the y vector to be used in backwards substition
    y = ForwardLU(A,b)
    #Backward substition is performed on the upper triangle of the matrix to produce the solution vector x.
    x = Backwards(A,y)
    return x

#Perform Forward Substition on a lower Triangle matrix where 
def ForwardChole(A,b):
    n = len(A[0])
    x = [0 for _ in range(n)]

    for k in range(n):
        x[k] = b[k]
        factor = 0.0
        for j in range(k-1):
            factor += A[k][j] * x[j]
        x[k] = (b[k] - factor)/A[k][k]
    return x

def ForwardLU(A,b):
    n = len(A[0])
    x = [0 for _ in range(n)]

    for k in range(n):
        x[k] = b[k]
        factor = 0.0
        for j in range(k-1):
            factor += A[k][j] * x[j]
        x[k] = (b[k] - factor)
    return x

def Backwards(A,b):
    n = len(b)
    x = [0 for i in range(n)]
    for k in range(n-1,-1,-1):
        x[k] = b[k]
        for j in range(k+1, n):
            x[k] -= A[k][j] * x[j]
        x[k] = x[k]/A[k][k]
        
    return x  

def GaussBackWard(A,b):
    Upper(A,b)
    solution = Backwards(A,b)
    return solution
# Given a symmetric positive definite n x n matrix A, this algorithm returns  the lower diagonal matrix.
def CholeskyDecomp(A):
    n = len(A)
    L = [[0.0 for i in range(n)]for i in range(n)]

    for k in range(n-1):
        A[k][k] = math.sqrt((A[k][k]))
        L[k][k] = A[k][k]

        for i in range(k + 1, n):
            A[i][k] = A[i][k]/A[k][k]
            L[i][k] = A[i][k]
        for j in range(k + 1, n):
            for i in range(j, n):
                A[i][j] = A[i][j] - (A[i][k] * A[j][k])
                L[i][j] = A[i][j]
        
    L[n-1][n-1] = math.sqrt(A[n-1][n-1])
    return L

def CholeskySolver(A,b):
    start = time.process_time()
    L = CholeskyDecomp(A)
    end = (time.process_time() - start)
    print("Factor Time: ", end)
    Lt = MatrixOperations.Transpose(L)
    y = ForwardChole(L,b)
    x = Backwards(Lt,y)
    
    return x
