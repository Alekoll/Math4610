# Software Manual For Vector Subtraction

**Routine Name:** Subtraction
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 VectorOperations.py`

**Description/Purpose:** Given A, B as vectors, Vector subtraction is defined as:

![](http://mathworld.wolfram.com/images/equations/VectorDifference/NumberedEquation1.gif)

**Input:** This routine requires two inputs as list: x,y
`Subtraction(x, y)`

**Output:** This routine returns a vector as a list.
```
[11, 17, 46]
```

**Usage/Example:** The routine requires two arguement. The routine returns a vector as a list.
```python3

 x = [23,34,53]
 y = [12, 17, 7]

 subtraction = VectorOperations.Subtraction(x,y)
 ```
Output from the line above:

`[11, 17, 46]`

**Implementation/Code:** The following code is for vector subtraction:

```python3 

def Subtraction(x,y):
    length = len(x)
    z = []

    for i in range(length):
        z.append(x[i] - y[i])

    return z


```
