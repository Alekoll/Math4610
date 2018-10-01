# Software Manual For Derivative Approximation

**Routine Name:** approxDeriv
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 approxDeriv.py`

**Description/Purpose:** This routine will approximate the derivative of a given function by using the definition of a derivative. 
![](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Clim%20h%20%5Cto%200%5Cfrac%7Bf%28a%20&plus;%20h%29%20-%20f%28a%29%7D%7Bh%7D)

**Input:** This routine requires three inputs: h, function as a lambda expression, and a. lambda expression are written as followed: ``` lambda arguments : expression ```

**Output:** This routine returns a floating point number as the approximated value

**Usage/Example:** The routine requires three arguments. The routine returns the approximated value.

```
 approxDeriv(0.0001, lambda x: x**2 - 3, 2)
 ```
Output from the line above:

`4.0001000000078335`

**Implementation/Code:** The following code is for approxDeriv(h, f, a).

```
#!/usr/bin/env python3

#approximates the derivate of a function. It takes 3 inputs: h, and expression written as a lambda , value
def approxDeriv(h, f, a):
    return (f(a+h) - f(a))/h



```
