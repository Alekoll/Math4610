from MatrixOperations import VectorMatrixMultiplication, Subtraction
from VectorOperations import InnerProduct,ScalarMultiplication,Magnitude
from MatrixNorms import InfNorm
from Gauss_Elim import GaussBackWard

def PowerMethod(A,v,stop):
    n = len(v)
    eigen = 0.0
    for i in range(0, stop):
        approx = VectorMatrixMultiplication(A,v)
        ScalarMultiplication(approx,1/Magnitude(approx))
        for j in range(n):
            v[j] = approx[j]
        eigen = InnerProduct(v, VectorMatrixMultiplication(A,v))
    return eigen

def InverseMethod(A,v,stop):
    n = len(v)
    norm = InfNorm(A)
  
    eigen = 0.0
    I = [[0 for i in range(n)]for i in range(n)]
    for i in range(n):
        I[i][i] = norm
    for i in range(stop):
       B = Subtraction(A, I)
       approx = GaussBackWard(B, v)
       ScalarMultiplication(approx, 1/Magnitude(approx))
       for j in range(n):
           v[j] = approx[j]
       eigen = InnerProduct(v, VectorMatrixMultiplication(A,v))
    return eigen


       
        