# Software Manual Forward Substitution 
**Routine Name:** ForwardLU or ForwardChole
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 Gauss_Elim.py`

**Description/Purpose:** Forward substition is the proccess of solving linear algebraic Equations for Lower triangle Matrices. and produces a solution vector.

ForwardLU: The main diagonal assumed to be 1's

ForwardChole: Does not assume the main diagonal are 1's

**Input:** These two routines requires two inputs: as 2-D list and list: 

`ForwardLU(A,b)`

`ForwardChole(A,b)`

**Output:** This routine produces the solution set of a lower triangle matrix.
 ```
[5.336337859106299, 9.968689988607814, 1.6182381137483264]
 ```

**Usage/Example:** The routine requires two arguement. The routine returns a list as the solution.

```python3 Taken from LU solver
  
  y = ForwardLU(A,b)

```

**Implementation/Code:** The following code ForwardLU:

```python3 

def ForwardLU(A,b):
    n = len(A[0])
    x = [0 for _ in range(n)]

    for k in range(n):
        x[k] = b[k]
        factor = 0.0
        for j in range(k-1):
            factor += A[k][j] * x[j]
        x[k] = (b[k] - factor)
    return x

```
**Implementation/Code:** The following code ForwadChole:

```python3 

def ForwardLU(A,b):
    n = len(A[0])
    x = [0 for _ in range(n)]

    for k in range(n):
        x[k] = b[k]
        factor = 0.0
        for j in range(k-1):
            factor += A[k][j] * x[j]
        x[k] = (b[k] - factor)/A[k][k]
    return x

```
