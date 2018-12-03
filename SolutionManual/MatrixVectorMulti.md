# Software Manual For Matrix Vector Multiplication

**Routine Name:** Matrix Vector
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 MatrixOperations.py`

**Description/Purpose:** Given: A an nxm matrix, x 1xm vector , Matrix Vector Multipliation is defined by: 

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/c9ee72cd113492a27f6f6f9279f2a93f2bf31c97)

**Input:** This routine requires two inputs Matrix and Vector :

`Scalar(A, x)`

**Output:** This routine returns a list contain the product:
```
[28, 104, 208]
```

**Usage/Example:** The routine requires two arguement. The routine returns a Matrix as a 2d list.
```python3

A = [[1,2,3],[5,7,11],[13,17,19]]
x = [2,4,6]
c = VectorMatrixMultiplication(A,x)
 ```
Output from the line above:

`[28, 104, 208]
`

**Implementation/Code:** The following code is for Matrix addition:

```python3 
def VectorMatrixMultiplication(A, x):
    row = len(A)
    col = len(A[0])
    product = [0]*row
    for j in range(col):
        rows = []
        for i in range(row):
            rows.append(A[i][j])
        
        scalar(rows, x[j])
        for i in range(row):
            product[i] += rows[i]
        
    return product
```
