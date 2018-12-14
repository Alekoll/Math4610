# Software Manual: Solving using Conjugate Method
**Routine Name:** Conjugate
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 GradientMethods.py`

**Description/Purpose:** Given: A (n x n), diagonally dominate, symmetric, and b solution set.  Used in sparse system when the matrix is too large to use direct methods.


**Input:** The routine requires two inputs: as 2-D list and list: 

`Conjugate(A,b)`

**Output:** This routine produces a vector with the solution.
 
 ```
[9.000000000230443, -9.999999998541085, 8.999999999871253]
 ```

**Usage/Example:** The routine requires two arguement. A, and b.
```
import BuildMatrix

A = BuildMatrix(3,10)
exact = CreateX(3,10)
b = Createb(A, exact)

approx = Conjugate(A,b)

```
Exact solution:

```
[9, -10, 9]
```

Solution from the algorithm:

```
[9.000000000230443, -9.999999998541085, 8.999999999871253]
```

The error from the exact solution was computed by taking the |norm2(approx) - norm2(exact)|:

```
8.447749166862195e-10

```

**Implementation/Code:** The following code is for solving a matrix using Jacobi Iteration

```python3 


def Conjugate(A,b):
    n = len(b)
    x0 = [1 for i in range(n)]
    r0 = Subtraction(b, VectorMatrixMultiplication(A,x0))
    p0 = deepcopy(r0)

    x1 = [0 for i in range(n)]
    r1 = [0 for i in range(n)]

    while(LengthNormInf(r0) > .000005):

        x1 = [0 for i in range(n)]
        r1 = [0 for i in range(n)]
        VM = VectorMatrixMultiplication(A,p0)

        alpha = InnerProduct(r0,r0)/InnerProduct(p0, VM)

        ScalarMultiplication(p0,alpha)
        ScalarMultiplication(VM, alpha)

        for i in range(n):
            x1[i] = x0[i] + p0[i]
            r1[i] = r0[i] - VM[i]
        if(LengthNormInf(r1) < .000005):
            return x1
        
        beta0 = InnerProduct(r1,r1)/InnerProduct(r0,r0)
        ScalarMultiplication(p0,beta0)

        p1 = [0 for i in range(n)]
        for i in range(n):
            p1[i] = r1[i] + p0[i]

        for i in range(n):
            r0[i] = r1[i]
            x0[i] = x1[i]
            p0[i] = p1[i]
    return x0

```
