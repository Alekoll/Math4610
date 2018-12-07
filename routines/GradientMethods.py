from VectorOperations import Subtraction, ScalarMultiplication, InnerProduct
from lengthnorms import LengthNormInf
from MatrixOperations import VectorMatrixMultiplication
from copy import deepcopy

def Steepest(A,b):
    n = len(b)
    x0 = [0 for i in range(n)]
    r = Subtraction(b, VectorMatrixMultiplication(A,x0))
    while(LengthNormInf(r) > .005):
        x1 = [0 for i in range(n)]
        r = Subtraction(b, VectorMatrixMultiplication(A,x0))
        alpha = InnerProduct(r,r)/InnerProduct(r,VectorMatrixMultiplication(A,r))
        ScalarMultiplication(r,alpha)
        for i in range(n):
            x1[i] = x0[i] + r[i]
        for i in range(n):
            x0[i] = x1[i]
    return x0

def Conjugate(A,b):
    n = len(b)
    x0 = [0 for i in range(n)]
    r0 = Subtraction(b, VectorMatrixMultiplication(A,x0))
    p0 = deepcopy(r0)

    while(LengthNormInf(r0) > .0005):
        x1 = [0 for i in range(n)]
        r1 = [0 for i in range(n)]
        VM = VectorMatrixMultiplication(A,p0)

        alpha = InnerProduct(r0,r0)/InnerProduct(p0, VM)
        ScalarMultiplication(p0,alpha)
        ScalarMultiplication(VM, alpha)

        for i in range(n):
            x1[i] = x0[i] + p0[i]
            r1[i] = r0[i] - VM[i]
        ScalarMultiplication(p0,1/alpha)
        beta0 = InnerProduct(r1,r1)/InnerProduct(r0,r0)
        p1 = [0 for i in range(n)]
        ScalarMultiplication(p0,beta0)
        for i in range(n):
            p1[i] = r1[i] + p0[0]
        for i in range(n):
            r0[i] = r1[i]
            x0[i] = x1[i]
            p0[i] = p1[i]
    return x0