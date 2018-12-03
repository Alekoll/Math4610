# Software Manual For Matrix Scalar Multiplication

**Routine Name:** Matrix Scalar
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 MatrixOperations.py`

**Description/Purpose:** Given: A an nxn matrix, c constant, Matrix Scalar Multipliation is defined by: 

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/249286d687770eadec5a02096535dcd814501b88)

**Input:** This routine requires two inputs Matrix and a Scalar:

`Scalar(A, alpha)`

**Output:** This routine returns None Object since it's a modification to A, but if printed this is the output:
```
[10, 20, 30]
[50, 70, 110]
[130, 170, 190]
```

**Usage/Example:** The routine requires two arguement. The routine returns a Matrix as a 2d list.
```python3

 A = [[1,2,3],[5,7,11],[13,17,19]]
 a = 10
 
 Scalar(A,a)


 ```
Output from the line above:

`[10, 20, 30]
[50, 70, 110]
[130, 170, 190]
`

**Implementation/Code:** The following code is for Matrix addition:

```python3 

def Scalar(A, alpha):
    row = len(A)
    col = len(A[0])

    for i in range(row):
        for j in range(col):
            A[i][j] *= alpha

    
```
