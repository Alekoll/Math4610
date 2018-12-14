# Software Manual Backward Substitution 
**Routine Name:** Backwards
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 Gauss_Elim.py`

**Description/Purpose:** Backward substitution is the proccess of solving linear algebraic Equations for Upper triangle Matrices. and produces a solution vector.

Assuming that the main diag

**Input:** These two routines requires two inputs: as 2-D list and list: 

`BackwardsLU(A,b)`

**Output:** This routine produces the solution set of a Upper triangle matrix.
 ```
[5.929437930284277, 1.2354697474013567, 2.8048190371250175]
 ```

**Usage/Example:** The routine requires two arguement. The routine returns a list as the solution.

```python3 Taken from Gaussian Solver
  
  x = Backwards(A,b)

```

**Implementation/Code:** The following code is for Backwards substitution:

```python3 

def Backwards(A,b):
    n = len(b)
    x = [0 for i in range(n)]
    for k in range(n-1,-1,-1):
        x[k] = b[k]
        for j in range(k+1, n):
            x[k] -= A[k][j] * x[j]
        x[k] = x[k]/A[k][k]
        
    return x  


```
