# Software Manual For Finding Roots from a Quadratic Equations

**Routine Name:** findRoots
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 findRoots.py`

**Description/Purpose:** This routine will solve the quadratic equation in the form of aX^2 + bX + cX^0 = 0 by using the quadratic formula.

**Input:** This routine takes three parameters. where the first parameter is the coefficient of the x^2 term, second is the coefficient of the X term, and the third is the coeffient of the X^0 term.

**Output:** This routine returns a list with two elements.

**Usage/Example:** The routine requires three arguments. The routine returns a list that contains the two values and prints.
```
 findRoots(1,5,6)
 ```
Output from the line above:

`[(-3+0j), (-2+0j)]`

The first value in the list is the one with the negative radical. The second value in the list contains the one with the positive radical.

**Implementation/Code:** The following code is for findRoots(a,b,c). Make sure to import cmath.

```
def findRoots(a,b,c):
    sqrt1 = (b**2) - (4*a*c)
    denom = 2*a
    negB = -b
    solutionList = []

    sol1 = (negB - cmath.sqrt(sqrt1))/denom

    sol2 = (negB + cmath.sqrt(sqrt1))/denom

    #solutionList[0] contains the negative value, and solutionList[1] contains the pos
    #value
    solutionList.append(sol1)
    solutionList.append(sol2)

    print(solutionList)
    return solutionList
```
