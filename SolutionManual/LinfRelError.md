# Software Manual For Computing Relative Error of linf norm.

**Routine Name:** RelErrorLengthNormInf
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 VectorErrors.py`

**Description/Purpose:** This routine will compute the relative error of two vectors where one vector is an approximate of the other.

**Input:** This routine requires two inputs: Approximate vector as a list, and an Exact vector as a list.
`AbsErrorLengthNormInf(approx, exact)`

**Output:** This routine returns a float precision value. below is an expmple of the output.
```
0.0012340000000001794
```

**Usage/Example:** The routine requires two arguement. The routine returns float value of the relative error.
```python3
Exact = [1,2,3,4,5,6,7,8,9]
Approx = [.987654,1.98888,2.988878, 3.9999857, 4.985443, 5.97979, 6.989978544, 7.9987, 8.998766]

absNorminf = VectorErrors.RelErrorLengthNormInf(Approx, Exact)
 ```
Output from the line above:

`0.0012340000000001794`

**Implementation/Code:** The following code is for absolute error of linf norms.

```python3

import lengthnorms, relError, absError

def RelErrorLengthNormInf(vectorX, vectorY):
    lengthX = lengthnorms.LengthNormInf(vectorX)
    lengthY = lengthnorms.LengthNormInf(vectorY)

    return relError.relError(lengthX, lengthY)
```
