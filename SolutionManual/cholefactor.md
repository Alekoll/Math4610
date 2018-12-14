# Software Manual Cholesky Factorization 
**Routine Name:** CholeskyDecomp
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 Gauss_Elim.py`

**Description/Purpose:** Given: A (n x n). Cholesky Factorization transform A into a Lower Triangle matrix and a product of the lower triangle matrix conjugate.

My version of the code, the factorization on produces the Lower triangle matrix without multiplying with the conjugate. That process happens when it is solved.

Ax = b is the same as: Lb = y, Lty = x

**Input:** The routine requires one inpute: as 2-D list: 

`CholeskyDecomp(A)`

**Output:** This routine produces new lower triangle matrix of A.
 
 ```
[576.1093646175177, 0.0, 0.0, 0.0, 0.0]
[10.749695075884711, 528.9881322447371, 0.0, 0.0, 0.0]
[14.8201027866791, 12.674553558694955, 675.8355719000592, 0.0, 0.0]
[5.2333813424499285, 13.086763812595368, 12.148771392199569, 624.7973717024568, 0.0]
[3.641669670467645, 9.729619338783534, 5.292280620414467, 4.867686635637213, 483.9073983131335]
 ```

**Usage/Example:** The routine requires one arguement. The routine a new matrix. The matrix used was 5 x 5 ,(Positive Definite), Symmetric.

```
A = BuildMatrix(5,10)
exact = CreateX(5,10)
b = Createb(A, exact)

C = CholeskyDecomp(A)

```

A:

```
[331902.0, 6193.0, 8538.0, 3015.0, 2098.0]
[6193.0, 279944.0, 6864.0, 6979.0, 5186.0]
[8538.0, 6864.0, 457134.0, 8454.0, 3754.0]
[3015.0, 6979.0, 8454.0, 390718.0, 3252.0]
[2098.0, 5186.0, 3754.0, 3252.0, 234326.0]

```

C:

```
[576.1093646175177, 0.0, 0.0, 0.0, 0.0]
[10.749695075884711, 528.9881322447371, 0.0, 0.0, 0.0]
[14.8201027866791, 12.674553558694955, 675.8355719000592, 0.0, 0.0]
[5.2333813424499285, 13.086763812595368, 12.148771392199569, 624.7973717024568, 0.0]
[3.641669670467645, 9.729619338783534, 5.292280620414467, 4.867686635637213, 483.9073983131335]
```

**Implementation/Code:** The following code is for Decomposing a matrix using Cholesky Factorization

```python3 

# Given a symmetric positive definite n x n matrix A, this algorithm returns  the lower diagonal matrix.
def CholeskyDecomp(A):
    n = len(A)
    L = [[0.0 for i in range(n)]for i in range(n)]

    for k in range(n-1):
        A[k][k] = math.sqrt((A[k][k]))
        L[k][k] = A[k][k]

        for i in range(k + 1, n):
            A[i][k] = A[i][k]/A[k][k]
            L[i][k] = A[i][k]
        for j in range(k + 1, n):
            for i in range(j, n):
                A[i][j] = A[i][j] - (A[i][k] * A[j][k])
                L[i][j] = A[i][j]
        
    L[n-1][n-1] = math.sqrt(A[n-1][n-1])
    return L
```
