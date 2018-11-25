# Software Manual For L2 Norm

**Routine Name:** lengthnorms.py
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 lengthnorms.py`

**Description/Purpose:** A norm is a function that assigns a length to a vector. L2 is defined by:

![](http://mathworld.wolfram.com/images/equations/L2-Norm/NumberedEquation2.gif)

**Input:** This routine requires a list as a vector.
`LengthNorm2(vector)`

**Output:** This routine returns the length.

**Usage/Example:** The routine requires single arguments. The routine returns the length value.

```python3
 testList = [3,54,656,43,23,64,76,32,1,25,45.232,4565.7685,674.9876]
 LengthNorm2(testList)
 ```
Output from the code above:

`
4663.802867786117
`

**Implementation/Code:** The following code is for finding L2 norm.

```python3

def LengthNorm2(vector):
    
    length2 = 0.0

    for element in vector:
        length2 += abs(element)**2
    
    return length2**(1/2)
```
