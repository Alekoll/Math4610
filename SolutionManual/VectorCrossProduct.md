# Software Manual For Vector Cross Product

**Routine Name:** CrossProduct
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 VectorOperations.py`

**Description/Purpose:** Given A, B as vectors of size 3, Vector cross product is defined as:

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/2a2f160ed91fcc66d751c2578a043745e9efcf22)

**Input:** This routine requires two inputs as list: x,y
`CrossProduct(x, y)`

**Output:** This routine returns a vector as a list.
```
[-663, 475, -17]
```

**Usage/Example:** The routine requires two arguement. The routine returns a vector as a list.
```python3

 x = [23,34,53]
 y = [12, 17, 7]

 crossProduct = VectorOperations.CrossProduct(x,y)
 ```
Output from the line above:

`[-663, 475, -17]`

**Implementation/Code:** The following code is for vector cross product:

```python3 

def CrossProduct(x, y):

    z1 = (x[1] * y[2]) - (x[2] * y[1])
    z2 = (x[2] * y[0]) - (x[0] * y[2])
    z3 = (x[0] * y[1]) - (x[1] * y[0])
    
    return [z1,z2,z3]

```
