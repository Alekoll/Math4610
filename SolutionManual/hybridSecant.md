# Software Manual For Hybrid Secant Method

**Routine Name:** hybridSecant.py
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 hybridSecant.py`

**Description/Purpose:** the Hybrid Secant method is a root-finding algorithm that combines the bisection method and secant method together to get faster convergence.

**Input:** This routine requires five inputs: function as a lambda expression, a as the left bound, b as the right bound, tolerence, and maximum iterations.
`HybridSecant(f, a, b, tol, maxIter)`

lambda expression are written as followed: 
```python3
lambda arguments: expression `
```

**Output:** This routine returns either a floating point number containing the approximated root or None object if the interval does not contain a root.

**Usage/Example:** The routine requires five arguments. The routine returns the approximate root value or None.

```python3
 print(hybridSecant(lambda x: x**2 - 3,-100, -1, pow(10, -15), 15))
 ```
Output from the code above:

`-1.7320508075688772`

**Implementation/Code:** The following code is for HybridNewton(f,fprime, a, b, tol, maxIter)

```python3

def hybridSecant(f, a, b, tol, maxIter):
  
    i = 0
    sec = None
    x = bisection.bisection(f, a, b, tol, 4)
    xa = x[0]
    xb = x[1]

    if(x is None):
        return None
    
    while (i < maxIter):
        
        i += 1
        
        sec = secant.Secant(f,xa, xb,tol,maxIter)

        if(sec is not None):
            return sec
        else:
            x = bisection.bisection(f, xa, xb, tol, 4)
            xa = x[0]
            xb = x[1]
```
