import random
from MatrixOperations import Transpose, MatrixMultiplication, VectorMatrixMultiplication
import Jacobi, GradientMethods, GaussSeidel, PowerMethods, Gauss_Elim
#Creates a matrix with three properties, n x n, Unified Random Variables, Symmetric, diagonally dominant
def BuildMatrix(n,x):
    C = [[abs(random.uniform(-x,x)) for _ in range(n)] for _ in range(n)]    
    for i in range(n):
        colSum = 0.0
        for j in range(n):
            colSum += abs(C[i][j])
        
        C[i][i] = (colSum * colSum)
    A = MatrixMultiplication(C,Transpose(C))

    return A

def Createx(n,x):
    return [abs(random.uniform(-x,x)) for _ in range(n)]

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

        print(Jacobi.Jacobi(A,b, [1 for _ in range(len(b))],30))
    
    if(method is "GuassSeidel"):
        print(GaussSeidel.GaussSeidel(A,b,[1 for _ in range(n)], 15))

    if(method is "Conjugate"):
        print(GradientMethods.Conjugate(A,b))
    
    if(method is "PowerMethod"):
        print(PowerMethods.PowerMethod(A, [1 for i in range(n)], 15))
    
    if(method is "InverseMethod"):
        print(PowerMethods.InverseMethod(A, [2 for i in range(n)], 1000))
        print(PowerMethods.PowerMethod(A, [2 for i in range(n)], 1000))
    
    if(method is "GaussBack"):
        print(Gauss_Elim.Backwards(A,b))
    if(method is "LU"):
        print(Gauss_Elim.LUDecomposition(A,b))
    if(method is "Chole"):
        print(Gauss_Elim.CholeskySolver(A,b))
    if(method is "cond"):
        print(PowerMethods.Condition2(A,[2 for i in range(n)], 1000))
BuildTest(5, 100, "cond")
