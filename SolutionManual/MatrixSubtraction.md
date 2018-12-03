# Software Manual For Matrix Subtraction

**Routine Name:** Matrix Subtraction
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 MatrixOperations.py`

**Description/Purpose:** Given A, B as nxn Matrices, the difference is  is defined by subtracting the entries of the same indices: C = A - B, C_ij = A_ij - B_ij



**Input:** This routine requires two inputs as 2-D list: A,B
`Subtraction(A,B)`

**Output:** This routine returns a Matrix as a 2d list.
```
[-1, -2, -3]
[2, 1, 2]
[8, 7, 4]

```

**Usage/Example:** The routine requires two arguement. The routine returns a Matrix as a 2d list.
```python3

 A = [[1,2,3],[5,7,11],[13,17,19]]
 
 B = [[2,4,6],[3,6,9],[5,10,15]]

 C = Subtraction(A,B)


 ```
Output from the line above:

`[-1, -2, -3]
[2, 1, 2]
[8, 7, 4]
`

**Implementation/Code:** The following code is for Matrix addition:

```python3 


def Subtraction(A, B):
    row = len(A)
    col = row

    C = [[0]* row for _ in range(row)]

    for i in range(row):
        for j in range(col):
            C[i][j] = A[i][j] - B[i][j]
    return C
    
```
