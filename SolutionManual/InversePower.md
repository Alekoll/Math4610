# Software Manual: Find Eigenvalue using Inverse Power method

**Routine Name:** InverseMethod
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 PowerMethods.py`

**Description/Purpose:** Given: A (n x n), diagonally dominate, and guess vector. The power method will converge to the closest eigenvalue in the direction of the guess vector.


**Input:** The routine requires 3 inputs: A, guess vector, maxiter: 

`InversePower(A, v, stop)`

**Output:** This routine produces the closest eigenvalue:
 
 ```
25534.35088001618
 ```

**Usage/Example:** The routine requires two arguement. A, and b.
```
import BuildMatrix

A = BuildMatrix(5,10)
exact = CreateX(5,10)
b = Createb(A, exact)
v = [2,2,2,2,2]

eigenvalue = Inversemethod(A,v,1000)

```
Eigenvalue:

```
25534.35088001618

```


**Implementation/Code:** The following code is for finding the largest Eigenvalue from a matrix

```python3 

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

```
