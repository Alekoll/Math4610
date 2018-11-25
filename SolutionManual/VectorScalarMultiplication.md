# Software Manual For Vector Scalar Product

**Routine Name:** ScalarProduct
 
**Author:** Alex Collantes
 
**Language:** Python 3.7 Can be compiled using python3.

For example,

`python3 VectorOperations.py`

**Description/Purpose:** Given: A as vector, c as constant,  Vector scalar multiplicaiton is defined as: c * A = (ca_1, ca_2, ca_3, ..., ca_n)


**Input:** This routine requires two inputs: A, c
`ScalarMutiplication(A, c)`

**Output:** This routine modifies vector A. Returns NONE
```
NONE
```


**Usage/Example:** The routine requires two arguement. The routine returns None since it modifies vector A.
```python3

 x = [23,34,53]
 
 VectorOperations.ScalarMultiplication(x,.5)
 ```
Result from the line above:

`[11.5, 17.0, 26.5]`

**Implementation/Code:** The following code is for vector subtraction:

```python3 

def ScalarMultiplication(x, scalar):
    
    for i in range(len(x)):
        
        x[i] *= scalar    
    

```
