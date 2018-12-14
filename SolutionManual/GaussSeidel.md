# Software Manual: Solving using Gauss-Seidel
**Routine Name:** GaussSeidel
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 GaussSeidel.py`

**Description/Purpose:** Given: A (n x n), diagonally dominate, and b solution set. Gauss-Seidel,
solves the system by iterating through until convergence=


**Input:** The routine requires two inputs: as 2-D list and list: 

`GaussSeidel(A,b)`

**Output:** This routine produces a vector with the solution.
 
 ```
[1.869793238793303, 72.58814400378849, -85.94731160768191]
 ```

**Usage/Example:** The routine requires two arguement. A, and b.
```
import BuildMatrix

A = BuildMatrix(3,100)
exact = CreateX(3,100)
b = Createb(A, exact)

approx = Gauss(A,b)

```
Exact solution:

```
[1.869793238796106, 72.58814400378833, -85.94731160768197]
```

Solution from the algorithm:

```
[1.869793238793303, 72.58814400378849, -85.94731160768191]
```

The error from the exact solution was computed by taking the |norm2(approx) - norm2(exact)|:

```
2.842170943040401e-14

```

**Implementation/Code:** The following code is for solving a matrix using Gauss-Seidel Iteration

```python3 


   def GaussSeidel(A, b):
        
    n = len(A)
    x = [1 for i in range(n)]

    k = 0

    while k < 15:
        x1 = [0 for _ in range(n)]
        for i in range(n):
            sum1 = 0
            sum2 = 0
            
            for j in range(i):
                sum1+=A[i][j]* x1[j]
               
            for j in range(i+1,n):
                sum2+=A[i][j]* x[j]
            x1[i] = (b[i]- sum1 - sum2)/A[i][i]
         
        k +=1
        for i in range(n):
            x[i] = x1[i]
    return x
```
