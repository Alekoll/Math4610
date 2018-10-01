# Software Manual For fixed point iteration

**Routine Name:** fixPoint.py
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 fixPoint.py`

**Description/Purpose:**  Algorithm: Fixed Point Iteration.

Given a scalar continuous function in one variable, f (x), select a function g(x) such that x satisfies f(x)=0 if and only if g(x)=x.Then:

1. Start from an initial guess x0.

2. For k = 0,1,2,..., set

xk+1 =g(xk) until xk+1 satisfies termination criteria.

**Input:** This routine requires fou inputs: function as a lambda expression, an intial guess x0, the tolerence, and maximum iterations.
`fixPoint(g, x0, tol, maxIter)`

lambda expression are written as followed: ``` lambda arguments : expression ```

**Output:** This routine will return an approximation of the root.

**Usage/Example:** The routine requires five arguments. The routine returns the root value.

```
 fixPoint(lambda x: (x+3)/(x+1), 2, tol, maxIter
```

Output from the code above:

`1.7320508100147276`

**Implementation/Code:** The following code is for fixPoint(g, x0, tol, maxIter)

```python3

def fixPoint(g,x0, tol, maxIter):
    i = 1
    error = 10 * tol

    while(error > tol and i < maxIter):
        i += 1
        x1 = g(x0)
        error = abs(x1 - x0)
        x0 = x1
    return x0

```
