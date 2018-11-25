# Software Manual For Frobenius Norm of a Matrix

**Routine Name:** MatrixNorms.py
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 MatrixNorms.py`

**Description/Purpose:** A norm is a function that assigns a length to a matrix. Frobenius Norm is defined by:

![](http://mathworld.wolfram.com/images/equations/FrobeniusNorm/NumberedEquation1.gif)

**Input:** This routine requires a 2d List.
`Frobenius(matrix)`

**Output:** This routine returns the norm as a float:
``

**Usage/Example:** The routine requires single arguments. The routine returns the length value.

```python3
 A = [[1,2,3],[5,6,8],[12,13,14]]
print(Frobenius(A))
 ```
Output from the code above:

`
25.45584412271571
`

**Implementation/Code:** The following code is for finding Frobenius norm.

```python3

def Frobenius(matrix):
    row = len(matrix)
    col = len(matrix[0])
    norm = 0.0

    for i in range(row):
        for j in range(col):
            norm += abs(matrix[i][j] * matrix[i][j])
    norm = norm**(.5)

    return norm

```
