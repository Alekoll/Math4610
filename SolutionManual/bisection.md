# Software Manual For Bisection Method

**Routine Name:** bisection.py
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 bisection.py`

**Description/Purpose:** The Bisection method is a root-finding algorithm that bisects an interval into subintervals for which the root is contained in.

**Input:** This routine requires five inputs: function as a lambda expression, a as the left bound, b as the right bound, the tolerence, and maximum iterations.
`bisection(f, a, b, tol, maxIter)`

lambda expression are written as followed: ``` lambda arguments : expression ```

**Output:** This routine returns either a floating point number containing the root or None object indicating that the interval does not contain the root.

**Usage/Example:** The routine requires five arguments. The routine returns the root value or None object.

```
 bisection(lambda x: x**2 - 3, .5, 3, pow(10, -15), 15)
 ```
 ```
 bisection(lambda x: x**2 - 3, 2, 3, pow(10, -15), 15)
 ```
Output from the first code above:

`1.7320508075688767`

Output from the second code above:
```
Sorry, but this interval does not contain a root
None
```
**Implementation/Code:** The following code is for bisection(f, a, b, tol, maxIter)

```python3

def bisection(f, a, b, tol, maxIter):
    #initalize the f(a) and (b) and the k value
    fa = f(a)
    fb = f(b)
    k = int(math.log2(tol/abs(b-a))/math.log2(1/2) + 1)
    
    if (maxIter == 4):
        k = maxIter
    
    # Check if the given interval contains the root
    if(fa * fb < 0.0):

        for i in range (0, k):
            c = .5*(a+b)
            fc = f(c)
            if(fa*fc < 0):
                b = c
                fb = fc
            else:
                a = c
                fa = fc
        
        return a
    else:
        print("Sorry, but this interval does not contain a root")
        return None 

```
