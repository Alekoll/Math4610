
from VectorOperations import Subtraction
from lengthnorms import LengthNormInf
from MatrixOperations import VectorMatrixMultiplication

def GaussSeidel(A, b):
        
    n = len(A)
    x = [1 for i in range(n)]

    k = 0

    while k < 15:
        x1 = [0 for _ in range(n)]
        for i in range(n):
            sum1 = 0
            sum2 = 0
            
            for j in range(i):
                sum1+=A[i][j]* x1[j]
               
            for j in range(i+1,n):
                sum2+=A[i][j]* x[j]
            x1[i] = (b[i]- sum1 - sum2)/A[i][i]
         
        k +=1
        for i in range(n):
            x[i] = x1[i]
    return x