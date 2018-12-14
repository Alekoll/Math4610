# Software Manual Solving Using LU Factorization.
**Routine Name:** LUDecomposition
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 Gauss_Elim.py`

**Description/Purpose:** Given: A (n x n). By performing Gaussian Elimination to reduce the matrix into [upper](https://github.com/Alekoll/Math4610/blob/master/SolutionManual/GaussianElim.md)
triangle matrix, and a lower triangle matrix.
We can solve the matrix by perform [Forward Sub](https://github.com/Alekoll/Math4610/blob/master/SolutionManual/ForwardSub.md) on A, then with the solution of that, perform
[backwards substition](https://github.com/Alekoll/Math4610/edit/master/SolutionManual/BackwardSub.md) on the Upper triangle of A. This process is known as LU Factorization.

Ax = b is the same as: Lb = y, Uy = x

**Input:** These two routines requires two inputs: as 2-D list and list: 

`LUDecomposition(A,b)`

**Output:** This routine produces the solution set of a given Matrix.
 
 ```
 [1.892671297531004, 6.812741123059347, 4.783394292178428]
 ```

**Usage/Example:** The routine requires two arguement. The routine returns a list as the solution.

```
A = BuildMatrix(3,10)
exact = CreateX(3,10)
b = Createb(A, exact)

solution = LUDecomposition(A,b)
```

**Implementation/Code:** The following code is for solving a matrix by transforming into an upper triangle matrix and using backward sub:

```python3 

# Guass-Elimination that returns a list of the multiples used. first use guassian elimination, then forward sub, then backward sub
def LUDecomposition(A,b):
   
    #perform Guassian Elimination where it modifies to a  upper and lower triangular matrix
    Upper(A,b)
    #Forward Substitution is performed on the modified Matrix, and produces the y vector to be used in backwards substition
    y = ForwardLU(A,b)
    #Backward substition is performed on the upper triangle of the matrix to produce the solution vector x.
    x = Backwards(A,y)
    return x


```
