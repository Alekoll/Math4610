# Software Manual For Computing Relative Error of a l1 norm.

**Routine Name:** RelErrorLengthNorm1
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 VectorErrors.py`

**Description/Purpose:** This routine will compute the relative error of two vectors where one vector is an approximate of the other.

**Input:** This routine requires two inputs: Approximate vector as a list, and an Exact vector as a list.
`AbsErrorLengthNorm1(approx, exact)`

**Output:** This routine returns a float precision value. below is an expmple of the output.
```
0.020931688639869606
```

**Usage/Example:** The routine requires two arguement. The routine returns float value of the relative error.
```python3
Exact = [1,2,3,4,5,6,7,8,9]
Approx = [.987654,1.98888,2.988878, 3.9999857, 4.985443, 5.97979, 6.989978544, 7.9987, 8.998766]

relNorm1 = VectorErrors.RelErrorLengthNorm1(Approx, Exact)
 ```
Output from the line above:

`0.020931688639869606`

**Implementation/Code:** The following code is for relative error of l1 norms.

```python3

import lengthnorms, relError, absError

def RelErrorLengthNorm1(vectorX, vectorY):
    lengthX = lengthnorms.LengthNorm1(vectorX)
    lengthY = lengthnorms.LengthNorm1(vectorY)

    return relError.relError(lengthX, lengthY)

```
