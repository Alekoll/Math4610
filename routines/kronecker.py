from Gauss_Elim import Upper
from MatrixOperations import Trace
import MatrixOperations

def kronecker(A,B):
    m = len(A[0])
    n = len(A)

    p = len(B[0])
    q = len(B)
    
    #Create a blank matrix full of zeros
    C = [[0 for i in range(m*p)] for i in range(n*q)]

    for i in range (m):

        for k in range(p):
        
            for j in range(n):

                for l in range(q):

                    C[i + l + 1][j+k +1] = A[i][j] * B[k][l]
    
    return C

def Determinant(A):
    def Det(A):
    deter = 0.0
    n = len(A[0])
    Upper(A,([0]*n))
    deter = Trace(A)
    return deter


A = [[1,2,3],[4,5,7],[7,5,2]]
B = [[4,5,5],[4,5,5],[5,5,5]]

C = kronecker(A,B)

for i in range(3):
    print(C[i])