# Software Manual For Trace of a Matrix

**Routine Name:** Matrix Trace
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 MatrixOperations.py`

**Description/Purpose:** Given A, an nxn matrix, Trace of a matrix is defined as: 

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/3e5b6e82272fc5eeca6d510388e0a2bd0a6c6463)

**Input:** This routine requires one input as 2-D list: A

`Trace(A)`

**Output:** This routine returns a float of the product of the main diagonal:
```
27.0
```

**Usage/Example:** The routine requires two arguement. The routine returns a Matrix as a 2d list.
```python3

 A = [[1,2,3],[5,7,11],[13,17,19]]

 C = Trace(A)


 ```
Output from the line above:

`27.0
`

**Implementation/Code:** The following code is for Matrix addition:

```python3 

def Trace(A):
    row = len(A)
    trace = 0.0
    for i in range(row):
        trace += A[i][i]
    return trace

    
```
