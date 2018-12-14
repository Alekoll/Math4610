# Software Manual: Solving using Jacobi Iteration
**Routine Name:** Jacobi
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 Jacobi.py`

**Description/Purpose:** Given: A (n x n), diagonally dominate, and b solution set. Jacobi method,
solves the system by iterating through until convergence. Named after Carl Gustav jacob Jacobi.


**Input:** The routine requires two inputs: as 2-D list and list: 

`Jacobi(A,b)`

**Output:** This routine produces a vector with the solution.
 
 ```
[2.9999999906567076, 2.000000001045583, -1.9999999999881048]
 ```

**Usage/Example:** The routine requires two arguement. A, and b.
```
import BuildMatrix

A = BuildMatrix(3,10)
exact = CreateX(3,10)
b = Createb(A, exact)

approx = Jacobi(A,b)

```
Exact solution:

```
[3, 2, -2]
```

Solution from the algorithm:

```
[2.9999999906567076, 2.000000001045583, -1.9999999999881048]
```

The error from the exact solution was computed by taking the |norm2(approx) - norm2(exact)|:

```
6.296831500662847e-09

```

**Implementation/Code:** The following code is for solving a matrix using Jacobi Iteration

```python3 

def Jacobi(A,b):
    n = len(b)
    x = [1 for i in range(n)]

    k = 0
    # while the difference of the Infinite norm of the difference between (Ax - b) > 1
    while(k < 15):
        for i in range(n):
            factor = 0.0
          
            for j in range(n):
             
                if (j != i):
                    factor += A[i][j] * x[j]
          
            x[i] = (b[i]-factor)/A[i][i]
        k += 1
    print(k)
    return x
```
