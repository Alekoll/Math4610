# Software Manual: Solving using Steepest Decent Method
**Routine Name:** Steepest
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 GradientMethods.py`

**Description/Purpose:** Given: A (n x n), diagonally dominate, and b solution set. The Gradient method, is an iterative method that
solves the system by taking steps proportional to teh negative of the gradient. 


**Input:** The routine requires two inputs: as 2-D list and list: 

`Steepest(A,b)`

**Output:** This routine produces a vector with the solution.
 
 ```
[9.000018306309078, 8.999999984313842, 2.9996157819958764]
 ```

**Usage/Example:** The routine requires two arguement. A, and b.
```
import BuildMatrix

A = BuildMatrix(3,10)
exact = CreateX(3,10)
b = Createb(A, exact)

approx = steepest(A,b)

```
Exact solution:

```
[9, 9, 3]
```

Solution from the algorithm:

```
[9.000018306309078, 8.999999984313842, 2.9996157819958764]
```

The error from the exact solution was computed by taking the |norm2(approx) - norm2(exact)|:

```
7.555174625650807e-05

```

**Implementation/Code:** The following code is for solving a matrix using Jacobi Iteration

```python3 

def Steepest(A,b):
    n = len(b)
    x0 = [0 for i in range(n)]
    r = Subtraction(b, VectorMatrixMultiplication(A,x0))
    while(LengthNormInf(r) > .00005):
        x1 = [0 for i in range(n)]
        r = Subtraction(b, VectorMatrixMultiplication(A,x0))
        alpha = InnerProduct(r,r)/InnerProduct(r,VectorMatrixMultiplication(A,r))
        ScalarMultiplication(r,alpha)
        for i in range(n):
            x1[i] = x0[i] + r[i]
        for i in range(n):
            x0[i] = x1[i]
    return x0

```
