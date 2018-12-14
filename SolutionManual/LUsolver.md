# Software Manual Gaussian Elimination solving with Backwards Substitution
**Routine Name:** GaussBackWard
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 Gauss_Elim.py`

**Description/Purpose:** Given: A (n x n). By performing Gaussian Elimination to reduce the matrix into [upper](https://github.com/Alekoll/Math4610/blob/master/SolutionManual/GaussianElim.md)
triangle matrix, we can solve the matrix by perform [backwards substition](https://github.com/Alekoll/Math4610/edit/master/SolutionManual/BackwardSub.md)

**Input:** These two routines requires two inputs: as 2-D list and list: 

`GaussBackWard(A,b)`

**Output:** This routine produces the solution set of a given Matrix.
 
 ```
 [5.929437930284277, 1.2354697474013567, 2.8048190371250175]
 ```

**Usage/Example:** The routine requires two arguement. The routine returns a list as the solution.

```
A = BuildMatrix(3,10)
exact = CreateX(3,10)
b = Createb(A, exact)

solution = GaussBackWard(A,b)
```

**Implementation/Code:** The following code is for solving a matrix by transforming into an upper triangle matrix and using backward sub:

```python3 

def GaussBackWard(A,b):
    Upper(A,b)
    solution = Backwards(A,b)
    return solution


```
