import BuildMatrix
import VectorErrors
import GradientMethods, GaussSeidel, Jacobi
import time
from lengthnorms import LengthNorm2 as norm2
from VectorErrors import AbsErrorLengthNorm2 as er

n = 640
x = 100000

A = BuildMatrix.BuildMatrix(n,x)
exact = BuildMatrix.Createx(n,x)
b = BuildMatrix.Createb(A,exact)

#Test The algorithm and time them using time.process_time on Unix based show CPU time spent on the current Process
start = time.process_time()
jacobi = Jacobi.Jacobi(A,b)
elapsed = (time.process_time() - start)
print("Jacobi Time: ", elapsed )


start = time.process_time()
gauss = GaussSeidel.GaussSeidel(A,b)
elapsed = (time.process_time() - start)

print("GaussSeidel Time:", elapsed)

start = time.process_time()
steepest = GradientMethods.Steepest(A,b)
elapsed = (time.process_time() - start)
print("Steepest: ", elapsed)

start = time.process_time()
conjugate = GradientMethods.Conjugate(A,b)
elapsed = (time.process_time() - start)
print("Conjugate: ", elapsed)

error = [er(jacobi, exact), er(gauss,exact), er(steepest, exact), er(conjugate, exact)]
print(error)

