# Software Manual For Hybrid Newton Method

**Routine Name:** hybridPython.py
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 hybridNewton.py`

**Description/Purpose:** the Hybrid Newton method is a root-finding algorithm that combines the bisection method and newton method together to get faster convergence.

**Input:** This routine requires six inputs: function as a lambda expression, the derivative, a as the left bound, b as the right bound, tolerence, and maximum iterations.
`HybridNewton(f, fprime, a, b, tol, maxIter)`

lambda expression are written as followed: 
```python3
lambda arguments: expression `
```

**Output:** This routine returns either a floating point number containing the approximated root or None object if the interval does not contain a root.

**Usage/Example:** The routine requires six arguments. The routine returns the approximate root value or None.

```python3
 HybridNewton(lambda x: x**2 - 3, lambda x: 2*x,-100,-1, pow(10, -15), 15)
 ```
Output from the code above:

`-1.7320508075688772`

**Implementation/Code:** The following code is for HybridNewton(f,fprime, a, b, tol, maxIter)

```python3

def HybridNewton (f, fprime, a, b, tol, maxIter):

    error = 10 * tol
    i = 0
    newton = None

    
    x = bisection.bisection(f, a, b, tol, 4)
    xa = x[0]
    xb = x[1]

    if(x is None):
        return None
    
    while (i < maxIter):

        i += 1
        x0 = .5*(xa + xb)
        
        newton = newtonMethod.NewtonMethod(f,fprime, x0, tol, maxIter)

        if(newton is not None):
    
            return newton
        else:
            x = bisection.bisection(f, xa, xb, tol, 4)
            xa = x[0]
            xb = x[1]
    
    return newton
```
