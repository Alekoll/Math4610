# Software Manual For linf Norm of a Matrix

**Routine Name:** InfNorm.py
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 MatrixNorms.py`

**Description/Purpose:** A norm is a function that assigns a length to a matrix. linf Norm is defined by:

![](http://mathworld.wolfram.com/images/equations/MatrixNorm/NumberedEquation5.gif)

**Input:** This routine requires a 2d List.
`Frobenius(matrix)`

**Output:** This routine returns the norm as a float:

`39.0`

**Usage/Example:** The routine requires single arguments. The routine returns the length value.

```python3
 A = [[1,2,3],[5,6,8],[12,13,14]]
print(Inf(A))
 ```
Output from the code above:

`
39.0
`

**Implementation/Code:** The following code is for finding linf norm.

```python3

def InfNorm(matrix):
    row = len(matrix)
    col = len(matrix[0])
    norm = 0.0
    rowSum = []

    for i in range(row):
        for j in range(col):
            norm += abs(matrix[i][j])
        rowSum.append(norm)
        norm = 0.0
    
    norm = max(rowSum)
    return norm
    
```
