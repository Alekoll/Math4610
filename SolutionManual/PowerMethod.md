# Software Manual: Find dominating Eigenvalue using Power method
**Routine Name:** PowerMethod
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 PowerMethods.py`

**Description/Purpose:** Given: A (n x n), diagonally dominate, and guess vector. The power method will converge to the highest eigenvalue in the direction of the guess vector.


**Input:** The routine requires 3 inputs: A, guess vector, maxiter: 

`PowerMethod(A, v, stop)`

**Output:** This routine produces the largest eigenvalue:
 
 ```
13350630684.410458
 ```

**Usage/Example:** The routine requires two arguement. A, and b.
```
import BuildMatrix

A = BuildMatrix(5,100)
exact = CreateX(5,100)
b = Createb(A, exact)
v = [2,2,2,2,2]

eigenvalue = Powermethod(A,v,100)

```
Eigenvalue:

```
13350630684.410458

```


**Implementation/Code:** The following code is for finding the largest Eigenvalue from a matrix

```python3 

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
```
