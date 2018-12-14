# Software Manual Vector Basis

**Routine Name:** Basis
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 Basis.py`

**Description/Purpose:** 
Produce an orthogonal basis given two vectors

**Input:** Two vectors as list

**Output:** This routine returns a list of list.

**Usage/Example:** The routine requires 2 arguments
```
 Basis(u,v)

 ```
Output from the line above:

```
[0.27539552761294706, 0.39779353988536803, 0.5201915521577889, 0.7037885705664203]
[-0.27539552761294706, 0.39779353988536803, 0.5201915521577889, 0.7037885705664203]
```

The first line is the projected vector and the bottom one is the orthogonal vector



**Implementation/Code:** The following code is vector basis:

```
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





```
