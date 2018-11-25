# Software Manual For Vector Addition

**Routine Name:** Addition
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 VectorOperations.py`

**Description/Purpose:** Given A, B as vectors, Vector addition is defined as:

![](http://mathworld.wolfram.com/images/equations/VectorAddition/NumberedEquation1.gif)

**Input:** This routine requires two inputs as list: x,y
`Additon(x, y)`

**Output:** This routine returns a vector as a list.
```
[35, 51, 60]
```

**Usage/Example:** The routine requires two arguement. The routine returns a vector as a list.
```python3

 x = [23,34,53]
 y = [12, 17, 7]

 additon = VectorOperations.Addition(x,y)
 ```
Output from the line above:

`[35, 51, 60]`

**Implementation/Code:** The following code is for vector addition:

```python3 

def Addition(x,y):
    length = len(x)
    z = []

    for i in range(length):
        z.append(x[i] + y[i])

    return z

```
