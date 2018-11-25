# Software Manual For l1 Norm of a Matrix

**Routine Name:** OneNorm.py
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 MatrixNorms.py`

**Description/Purpose:** A norm is a function that assigns a length to a matrix. Frobenius Norm is defined by:

![](http://mathworld.wolfram.com/images/equations/MatrixNorm/NumberedEquation3.gif)

**Input:** This routine requires a 2d List.
`Frobenius(matrix)`

**Output:** This routine returns the norm as a float:

`25.0`

**Usage/Example:** The routine requires single arguments. The routine returns the length value.

```python3
 A = [[1,2,3],[5,6,8],[12,13,14]]
print(OneNorm(A))
 ```
Output from the code above:

`
25.0
`

**Implementation/Code:** The following code is for finding l1 norm.

```python3

def OneNorm(matrix):
    row = len(matrix)
    col = len(matrix[0])
    norm = 0.0
    colSum = []

    for j in range(col):
        for i in range(row):
            norm += abs(matrix[i][j])
        colSum.append(norm)
        norm = 0.0
    
    norm = max(colSum)
    return norm


```
