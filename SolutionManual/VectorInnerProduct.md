# Software Manual For Vector Inner Product

**Routine Name:** InnerProduct
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 VectorOperations.py`

**Description/Purpose:** Given A, B as vectors, Vector inner product is defined as:

![](http://mathworld.wolfram.com/images/equations/DotProduct/Inline30.gif)

**Input:** This routine requires two inputs as list: x,y
`InnerProduct(x, y)`

**Output:** This routine returns a floating point value.
```
1225.0

```

**Usage/Example:** The routine requires two arguement. The routine returns a float.
```python3

 x = [23,34,53]
 y = [12, 17, 7]

 innerProduct = VectorOperations.InnerProduct(x,y)
 ```
Output from the line above:

`1225.0`

**Implementation/Code:** The following code is for vector subtraction:

```python3 

def InnerProduct(x, y):
    
    length = len(x)
    z = 0.0

    for i in range (length):
        z += x[i] * y[i]
    
    return z

```
