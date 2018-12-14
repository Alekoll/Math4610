# Software Manual Gaussian Elimination (n x n)
**Routine Name:** Upper
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 Gauss_Elim.py`

**Description/Purpose:** Gaussian Elmination (Also known as row reduciton) is a set of steps for solving systems of linear equations by swapping two rows, scaling by a nonzero, and adding rows. It has many applications by finding the rank of a matrix, calculating determinant, finding inverse...

Our Algorithm for Gaussian Elimination is used to find the upper triangle matrix with main. The factors of the lower Triangle matrix are also saved and a modified version of Forward substition can produce a solution.


**Input:** This routine requires two inputs: as 2-D list and list: 

`Upper(A,b)`


**Output:** This routine overwrites the origanl matrix and it's solution:
 
 `
[95733.61704095405, 2454.1184123621165, 3643.332798515107]

[-0.02563486566387923, 48345.45374147545, 3035.8599393770673]

[-0.03805698469490105, -0.06279514834240991, 69283.25119228476]

 `

**Usage/Example:** The routine requires two arguement. The routine returns the same modified matrix.

```python3
Gauss_Elim.Upper(A,b)
 ```

A before:


`[95733.61704095405, 2454.1184123621165, 3643.332798515107]

[2454.1184123621165, 48408.364737299606, 3129.2562862358072]

[3643.332798515107, 3129.2562862358072, 69612.54272807624]
`

A after:

`
[95733.61704095405, 2454.1184123621165, 3643.332798515107]

[-0.02563486566387923, 48345.45374147545, 3035.8599393770673]

[-0.03805698469490105, -0.06279514834240991, 69283.25119228476]
`

**Implementation/Code:** The following code Gaussian Elimination:

```python3 
def Upper(A,b):
    n = len(A[0])
    for k in range(n-1):
        for i in range(k+1, n):
            factor = A[i][k]/A[k][k]
            A[i][k] = -factor
            for j in range(k+1, n):
                A[i][j] = A[i][j] -(factor*A[k][j])
            b[i] -= factor*b[k]

```
