# Software Manual: Matrix Generator
**Routine Name:** Build Matrix
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 BuildMatrix.py`

**Description/Purpose:** Create a matrix and it's solution set to test various alorgithms. 

To build a matrix, there are 3 parts:

1. Creating a matrix that is diagonal dominate, symmetric, and Randomly uniformly distributed.

1. Create the exact solution set, the x in Ax = b

1. Create the b in Ax = b 

**Input:** Three routines have inputs

BuildMatrix: n, number of rows. x, the range in which the random numbers will be distributed.

`BuildMatrix(n,x)`

Createx: same inputs as BuildMatrix:

 `Createx(n,x)`
 
Createb: A, as the recently created matrix. Exact, as the newly created exact solution.

`Createb(A,x)`


**Output:** Three routines have outputs:

BuildMatrix: (n x n) that is diagonally dominate and symmetric.

```
[50665.0, 2000.0, 1398.0]
[2000.0, 65589.0, 3631.0]
[1398.0, 3631.0, 50705.0]
```

Createx: Vector with exact values.

```
[6, 5, 6]
```

Createb: Vector with solution.

```
[322378.0, 361731.0, 330773.0]
```



**Usage/Example:**
```
A = BuildMatrix(3,10)

exact = Createx(3,10)

b = Createb(A,exact)
```

**Implementation/Code:** BuildMatrix

```python3 

def BuildMatrix(n,x):
    C = [[random.randint(1,x) for _ in range(n)] for _ in range(n)]    
    for i in range(n):
        colSum = 0.0
        for j in range(n):
            colSum += abs(C[i][j])
        
        C[i][i] = (colSum * colSum)
    A = MatrixMultiplication(C,Transpose(C))

    return A
   
```


**Implementation/Code:** Createx

```python3 

def Createx(n,x):
    return [random.randint(1,x) for _ in range(n)]

```


**Implementation/Code:** Createb

```python3 
def Createb(A,x):
    b = VectorMatrixMultiplication(A,x)
    return b
```
