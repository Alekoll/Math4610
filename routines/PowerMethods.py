from MatrixOperations import VectorMatrixMultiplication, Subtraction
from VectorOperations import InnerProduct,ScalarMultiplication,Magnitude
from MatrixNorms import InfNorm
import lengthnorms
import copy
import Gauss_Elim

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

    z = copy.deepcopy(v)
    ScalarMultiplication(z,1/lengthnorms.LengthNorm2(v))

    y = Gauss_Elim.LUDecomposition(A,z)

    temp = InnerProduct(z, y)
    k = 0

    while k < stop:

        
        ScalarMultiplication(y, 1/lengthnorms.LengthNorm2(y))
        z = Gauss_Elim.LUDecomposition(A,y)
    
        temp1 = InnerProduct(z,y)
    
        temp = temp1
        for i in range(len(z)):
            y[i] = z[i]
        k += 1
        
    return 1/temp1

def Condition2(A,v,stop):

    eigen1 = PowerMethod(A, v, stop)
    eigen2 = InverseMethod(A,v,stop)
    return abs(eigen1/eigen2)



       
        