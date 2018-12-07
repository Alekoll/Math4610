
from VectorOperations import Subtraction
from lengthnorms import LengthNormInf
from MatrixOperations import VectorMatrixMultiplication

def GaussSeidel(A,b):
    n = len(b)
    x = [1 for i in range(n)]

    k = 0
    while(LengthNormInf(Subtraction(VectorMatrixMultiplication(A,x),b))> 1):
        for i in range(n):
            factor = 0.0
            for j in range(n):
                if (j != i):
                    factor += A[i][j] * x[j]
            x[i] = (b[i]-factor)/A[i][i]
        k += 1

    return x
