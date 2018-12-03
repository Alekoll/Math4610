# Software Manual For Transpose of a Matrix

**Routine Name:** Matrix Transpose
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 MatrixOperations.py`

**Description/Purpose:** Given A, an nxm matrix, transpose of a matrix is defined as: 

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/9b0864ad54decb7f1b251512de895b40545facf5)

**Input:** This routine requires one input as 2-D list: A
`Transpose(A)`

**Output:** This routine returns a Matrix as a 2d list where the rows and columns have been swapped
```
[1, 5, 13]
[2, 7, 17]
[3, 11, 19]

```

**Usage/Example:** The routine requires two arguement. The routine returns a Matrix as a 2d list.
```python3

 A = [[1,2,3],[5,7,11],[13,17,19]]

 C = Transpose(A)


 ```
Output from the line above:

`[1, 5, 13]
[2, 7, 17]
[3, 11, 19]
`

**Implementation/Code:** The following code is for Matrix addition:

```python3 

def Transpose(A):
    row = len(A)
    col = len(A[0])
    #creating an empty list
    transpose = []
    for j in range (col):
        rows = []
        for i in range (row):
            element = A[i][j]
            rows.append(element)
        transpose.append(rows)

    return transpose
    
```
