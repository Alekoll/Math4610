# Software Manual For Linfity Norm

**Routine Name:** lengthnorms.py
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 lengthnorms.py`

**Description/Purpose:** A norm is a function that assigns a length to a vector. Linf is defined by:

![](http://mathworld.wolfram.com/images/equations/L-Infinity-Norm/NumberedEquation2.gif)

**Input:** This routine requires a list as a vector.
`LengthNormInf(vector)`

**Output:** This routine returns the length.

**Usage/Example:** The routine requires single arguments. The routine returns the length value.

```python3
 testList = [3,54,656,43,23,64,76,32,1,25,45.232,4565.7685,674.9876]
 LengthNormInf(testList)
 ```
Output from the code above:

`
4565.7685
`

**Implementation/Code:** The following code is for finding Linf norm.

```python3
def LengthNormInf(vector):

    lengthInf = max(vector)

    return float(lengthInf)
```
