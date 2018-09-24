# Software Manual For Newton Method

**Routine Name:** newtonMethod.py
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 newtonMethod.py`

**Description/Purpose:** the Newton's method is a root-finding algorithm that takes a function, the derivative of the function, and a nearby intial guess x0, to approximate a root. If x0 is close, 
then x1 will be closer to the root. The algorithm can be summarized as:

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/710c11b9ec4568d1cfff49b7c7d41e0a7829a736)

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
