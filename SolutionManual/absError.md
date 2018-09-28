# Software Manual For Absolute Error

**Routine Name:** absError
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 absError.py`

**Description/Purpose:** This routine will compute the float precision value of the difference between a machine precision number, x, and an "exact" value, y. Using the definition of abslute error: |x-y|.

**Input:** This routine requires two inputs: Approximate value, and an Exact value.
`absError(x, y)`

**Output:** This routine returns a float precision value of |x-y|. below is an expmple of the output.
```
1.828459045061237e-06
```

**Usage/Example:** The routine requires two arguement. The routine returns float value of the absolute error.
```
absE = absError(2.71828, cmath.exp(1))
print(absE)
 ```
Output from the line above:

`1.828459045061237e-06`

**Implementation/Code:** The following code is for absError(x,y).

```
def absError(x, y):
    
    return abs(x - y)

```
