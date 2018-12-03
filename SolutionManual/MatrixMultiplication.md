# Software Manual For Matrix Multiplication

**Routine Name:** MatrixMultiplication
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 MatrixOperations.py`

**Description/Purpose:** Given: A n x m matrix, B m x p  matrix , Matrix Multipliation is defined by: 


![](http://mathworld.wolfram.com/images/equations/MatrixMultiplication/NumberedEquation3.gif) 

Where

![](http://mathworld.wolfram.com/images/equations/MatrixMultiplication/NumberedEquation1.gif)

**Input:** This routine requires two inputs Matrix and Matrix :

`MatrixMultiplication(A, x)`

**Output:** This routine returns a list contain the product of the two matrices:
```
[30, 36, 42]
[110, 133, 156]
[214, 263, 312]
```

**Usage/Example:** The routine requires two arguement. The routine returns a Matrix as a 2d list.
```python3

A = [[1,2,3],[5,7,11],[13,17,19]]
B = [[1,2,3],[4,5,6],[7,8,9]]
C = MatrixMultiplication(A,B)
 ```
Output from the line above:

`[30, 36, 42]
[110, 133, 156]
[214, 263, 312]
`

**Implementation/Code:** The following code is:

```python3 
def MatrixMultiplication(A,B):
    row = len(A)
    col = len(B[0])
    m = len(A[0])
    
    C = [[0] * row for i in range(col)]
    
    for i in range(row):
        for j in range(col):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    
    return C
```
