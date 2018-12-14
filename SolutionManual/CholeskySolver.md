# Software Manual Solving With Cholesky Factorization 
**Routine Name:** CholeskySolver
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 Gauss_Elim.py`

**Description/Purpose:** Given: A (n x n) and b solution set. Factorizing A by [Cholesky Factorization]() we can solve Ax = b.


My version of the code, the factorization on produces the Lower triangle matrix without multiplying with the conjugate. That process happens when it is solved.

Ax = b is the same as: Lb = y, Lty = x

**Input:** The routine requires two inputs: as 2-D list and list: 

`CholeskySolver(A,b)`

**Output:** This routine produces a vector with the solution.
 
 ```
[8.982360813094676, 4.516968513145889, 7.105153804910922]
 ```

**Usage/Example:** The routine requires one arguement. The routine a new matrix. The matrix used was 3 x 3 ,(Positive Definite), Symmetric.

```
A = BuildMatrix(3,10)
exact = CreateX(3,10)
b = Createb(A, exact)

solution = CholeskySolver(A,b)

```
Exact solution:

```
[9, 4, 7]
```

Solution from the algorithm:

```
[8.982360813094676, 4.516968513145889, 7.105153804910922]
```

**Implementation/Code:** The following code is for solving a matrix using Cholesky Factorization

```python3 

def CholeskySolver(A,b):
    L = CholeskyDecomp(A)
    Lt = MatrixOperations.Transpose(L)
    y = ForwardChole(L,b)
    x = Backwards(Lt,y)
    
    return x

```
