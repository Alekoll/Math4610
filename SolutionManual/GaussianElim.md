# Software Manual Kronecker Product
**Routine Name:** Kronecker Product
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 kronecker.py`

**Description/Purpose:** Given: A,B Matices, the Kronecker producted is a generalization of the outer product. Kronecker should not be confused with traditional matrix multiplication. If A (m x n) and B (p x q), then the Kronecker product A ⊗ B is the (mp x nq) blcok matrix.

**Input:** This routine requires two inputs as 2-D list and 2-D list: 

`kronecker(A,B)`

**Output:** This routine returns a new Matrix.

```
A = [[1,2,3],[4,5,7],[7,5,2]]
B = [[4,5,5],[4,5,5],[5,5,5]]

C = kronecker(A,B)
```
**Usage/Example:** The routine requires two arguement. The routine returns a Matrix as a 2d list.
```python3
C = kronecker(A,B)
 ```
Output from the line above:

`[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 4, 4, 5, 10, 15, 0, 0, 0]
[0, 16, 16, 20, 25, 35, 0, 0, 0]
`

**Implementation/Code:** The following code is for Determinant:

```python3 

def kronecker(A,B):
    m = len(A[0])
    n = len(A)

    p = len(B[0])
    q = len(B)
    
    #Create a blank matrix full of zeros
    C = [[0 for i in range(m*p)] for i in range(n*q)]

    for i in range (m):

        for k in range(p):
        
            for j in range(n):

                for l in range(q):

                    C[i + l + 1][j+k +1] = A[i][j] * B[k][l]
    
    return C

```
