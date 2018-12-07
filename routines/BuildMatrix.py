import random
from MatrixOperations import Transpose, MatrixMultiplication, VectorMatrixMultiplication
import Jacobi, GradientMethods, GaussSeidel, PowerMethods, Gauss_Elim
#Creates a matrix with three properties, n x n, Unified Random Variables, Symmetric, diagonally dominant
def BuildMatrix(n,x):
    C = [[random.uniform(-x,x) for _ in range(n)] for _ in range(n)]    
    for i in range(n):
        colSum = 0.0
        for j in range(n):
            if(i is not j):
                colSum += abs(C[i][j])
        a = abs(C[i][i])
        if(a < colSum):
           C[i][i] = colSum * colSum
    A = MatrixMultiplication(C, Transpose(C))

    return A

def Createx(n,x):
    return [random.uniform(-x,x) for _ in range(n)]

def Createb(A,x):
    b = VectorMatrixMultiplication(A,x)
    return b

def BuildTest(n,x,method):
    A = BuildMatrix(n,x)
    exact = Createx(n,x)
    print(exact)
    b = Createb(A,exact)

    if(method is "Steepest"):
        print(GradientMethods.Steepest(A,b))
        
    if(method is "Jacobi"):

        print(Jacobi.Jacobi(A,b))
    
    if(method is "GuassSeidel"):
        print(GaussSeidel.GaussSeidel(A,b))

    if(method is "Conjugate"):
        print(GradientMethods.Conjugate(A,b))
    
    if(method is "PowerMethod"):
        print(PowerMethods.PowerMethod(A, [1 for i in range(n)], 15))
    
    if(method is "InverseMethod"):
        print(PowerMethods.InverseMethod(A, [2 for i in range(n)], 100))
        print(PowerMethods.PowerMethod(A, [2 for i in range(n)], 100))
    
    if(method is "GaussBack"):
        print(Gauss_Elim.Backwards(A,b))
    if(method is "LU"):
        print(Gauss_Elim.LUDecomposition(A,b))
    if(method is "Chole"):
        print(Gauss_Elim.CholeskySolver(A,b))


BuildTest(3,100,'LU')
