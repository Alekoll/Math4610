import lengthnorms, VectorOperations
import copy

def Basis(u,v):
    temp = copy.deepcopy(u)

    VectorOperations.ScalarMultiplication(temp, VectorOperations.InnerProduct(temp,v)/lengthnorms.LengthNorm2(temp)**2)
    VectorOperations.ScalarMultiplication(temp, 1/lengthnorms.LengthNorm2(temp))

    orthogonal = copy.deepcopy(temp)
    orthogonal[0] *= -1

    return temp, orthogonal

u = [2,3,5,7]
v = [9,13,17,23]

base = Basis(v,u)

print(base[0])
print(base[1])


