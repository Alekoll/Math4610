import BuildMatrix
import VectorErrors
import Gauss_Elim
import time
from lengthnorms import LengthNorm2 as norm2
from VectorErrors import AbsErrorLengthNorm2 as er

n = 640
x = 100000

A = BuildMatrix.BuildMatrix(n,x)
print("complete")
exact = BuildMatrix.Createx(n,x)
b = BuildMatrix.Createb(A,exact)

start = time.process_time()
approx = Gauss_Elim.CholeskySolver(A,b)
end = (time.process_time() - start)

print("Finish Time: ", end)

print(er(approx, exact))



