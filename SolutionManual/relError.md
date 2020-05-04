# Software Manual For Relative Error

**Routine Name:** relError
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 relError.py`

**Description/Purpose:** This routine will compute the float precision value of the difference between a machine precision number, x, and an "expect" value, y divided by y Using the definition of relative error: |y-x|/|y|.

**Input:** This routine requires two inputs: Approximate value, and an Exact value.
`relError(x, y)`

**Output:** This routine returns a float precision value of |x-y|/|y|. below is an expmple of the output.
```
3.0477314336577383e-07
```

**Usage/Example:** The routine requires two arguement. The routine returns float value of the relative error.
```
relE = relError(2.718281, cmath.exp(1))
print(relE)
 ```
Output from the line above:

`3.0477314336577383e-07`

**Implementation/Code:** The following code is for relError(x,y). 

```
def relError(x, y):
    
    return abs((x-y)/y)

```
