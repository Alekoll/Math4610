# Software Manual For Determinant of a Matrix

**Routine Name:** Matrix Determinant
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 MatrixOperations.py`

**Description/Purpose:** Given A, an nxn matrix, Determinant of a matrix is defined as the product of the diagonal of an Upper triangle matrix. The first step is to use Guassian Elimination to find the upper triangle matrix, then take the trace of the matrix. 

**Input:** This routine requires one input as 2-D list: A

`Determinant(A)`

**Output:** This routine returns a float of the product of the main diagonal:
```
-10.0
```

**Usage/Example:** The routine requires two arguement. The routine returns a Matrix as a 2d list.
```python3
A = [[1,2,3],[5,7,11],[13,17,19]]
determinant = Det(A)
 ```
Output from the line above:

`-10.0
`

**Implementation/Code:** The following code is for Determinant:

```python3 

def Det(A):
    deter = 0.0
    n = len(A[0])
    Upper(A,([0]*n))
    deter = Trace(A)
    return deter

    
```
