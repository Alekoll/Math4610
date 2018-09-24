# Software Manual For Derivative Approximation

**Routine Name:** approxDeriv
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 approxDeriv.py`

**Description/Purpose:** This routine will approximate the derivative of a given function by using the definition of a derivative. 
\frac{f(x+h) - f(x)}{h}

**Input:** There are three inputs: 

**Output:** This routine returns a double precision value for the number of decimal digits that can be represented on the computer being queried.

**Usage/Example:** The routine requires no arguments. The routine returns the value of the precision in terms of the smallest number that can be represented. 

```
 DmacEp()
 print('Digits ', iPow, ' Machine Ep: ' , Dep)
 ```
Output from the line above:

`Digits  53 Machine Ep:  1.1102230246251565e-16`

The first value (53) is the number of binary digits that define the machine epsilon and the second is related to the decimal version of the same value. The number of decimal digits that can be represented is roughly eight (E-16 on the end of the second value).



**Implementation/Code:** The following code is for DmacEps(). Make sure to import cmath

```
def DmacEp():
    
    Dep = 1.0
    one = 1.0
    appOne = one + Dep

    iPow = 0
    for i in range(1,1000):
        iPow = 1 + iPow
        Dep = Dep/2
        appOne = one + Dep
        if(abs(appOne - one) == 0.0):
            break
    print('Digits ', iPow, ' Machine Ep: ' , Dep)
    return Dep


```
