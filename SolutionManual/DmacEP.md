# Software Manual For Double Precision

**Routine Name:** DmacEP
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 DmacEp.py`

**Description/Purpose:** This routine will compute the double precision value for the machine epsilon or the number of digits in the representation of real numbers in double precision. This is a routine for analyzing the behavior of any computer. This usually will need to be run one time for each computer.

**Input:** No inputs

**Output:** This routine returns a double precision value for the number of decimal digits that can be represented on the computer being queried.

**Usage/Example:** The routine requires no arguments. The routine returns the value of the precision in terms of the smallest number that can be represented. 

```
 def DmacEp()
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
