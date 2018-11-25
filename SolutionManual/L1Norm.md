# Software Manual For l1 Norm

**Routine Name:** lengthnorms.py
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 lengthnorms.py`

**Description/Purpose:** A norm is a function that assigns a length to a vector. L1 is defined by:

![](http://mathworld.wolfram.com/images/equations/L1-Norm/NumberedEquation2.gif)

**Input:** This routine requires five inputs: function as a lambda expression, derivative of the function as a lambda expression, x0 as an inital guess, the tolerence, and maximum iterations.
`NewtonMethod(f, fprime, x0, tol, maxIter)`

lambda expression are written as followed: 
```python3
lambda arguments: expression `
```

**Output:** This routine returns either a floating point number containing the root or None object indicating that maximum amount of iterations has been met and solution did not converge.

**Usage/Example:** The routine requires five arguments. The routine returns the root value or None object.

```python3
 newtonMethod(lambda x: x**2 - 3, lambda x: 2*x, .5, pow(10, -15), 15)
 ```
Output from the code above:

`1.7320508075688772`

**Implementation/Code:** The following code is for NewtonMethod(f, fprime, x0, tol, maxIter)

```python3
def NewtonMethod(f, fPrime, x0, tol, maxIter):
    
    i = 1
    error = 10 * tol
    
    while (error > tol and i <= maxIter):
    
        i = i + 1
        x1 = x0 - f(x0)/fPrime(x0)
        error = abs(x1 - x0)
        x0 = x1
        
    if i == maxIter:
    
        print("I'm sorry, but there was not a root near by")
        return None
        
    else: return x0
```
