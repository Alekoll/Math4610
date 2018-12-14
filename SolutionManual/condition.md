# Software Manual: 2-Condition of a Matrix

**Routine Name:** Condition
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 PowerMethods.py`

**Description/Purpose:** Given: A (n x n), The 2-condition of a matrix is: |eigen1/eigen2| where eigen1 > eigen2


**Input:** The routine requires 3 inputs: A, guess vector, maxiter: 

`Condition(A, v, stop)`

**Output:** This routine produces the rato of the eigenvalues:
 
 ```
7.382320955537891
 ```

**Usage/Example:** The routine requires two arguement. A, and b.
```
import BuildMatrix

A = BuildMatrix(5,100)
exact = CreateX(5,100)
b = Createb(A, exact)
v = [2,2,2,2,2]

condition = Condition(A,v,100)

```
Condition number:

```
7.382320955537891

```


**Implementation/Code:** The following code is for finding the largest Eigenvalue from a matrix

```python3 
def Condition2(A,v,stop):

    eigen1 = PowerMethod(A, v, stop)
    eigen2 = InverseMethod(A,v,stop)
    return abs(eigen1/eigen2)

```
