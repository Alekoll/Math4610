# Software Manual For Single Precision

**Routine Name:** SmacEP
 
**Author:** Alex Collantes
 
**Language:** C++ Can be compiled using G++ Compiler.

For example,

`g++ SmacEp.cpp`

will produce ./a.exe That can be executed. If you want a different name, the following will work better.

`g++ -o Smacp SmacEp.cpp`

**Description/Purpose:** This routine will compute the single precision value for the machine epsilon or the number of digits in the representation of real numbers in single precision. This is a routine for analyzing the behavior of any computer. This usually will need to be run one time for each computer.

**Input:** There are no inputs needed in this case. Even though there are arguments supplied, the real purpose is to return values in those variables.

**Output:** This routine returns a single precision value for the number of decimal digits that can be represented on the computer being queried.

**Usage/Example:** The routine has two arguments needed to return the values of the precision in terms of the smallest number that can be represented. Since the code is written in terms of a C++ methods, the values of the machine machine epsilon and the power of two that gives the machine epsilon. The first argument is a single precision, a float value and the second is an integer.

```
 void SmacEp(float Sep, int iPow)
 std::cout << "Digits: " << iPow << " Machine Ep: " << Sep << endl;
 ```
Output from the line above:

`Digits: 24 Machine Ep: 5.96046e-08`

The first value (24) is the number of binary digits that define the machine epsilon and the second is related to the decimal version of the same value. The number of decimal digits that can be represented is roughly eight (E-08 on the end of the second value).



**Implementation/Code:** The following code is for SmacEps()

```
//Calculates Single Precision
void SmacEp(float Sep, int iPow){
    //Set values close to 1
    float one = 1.0;
    Sep = 1.0;
    float appOne = one + Sep;
    
    iPow = 0;
    for( int i = 1; i < 1000; i++){
        iPow += 1;
        Sep = Sep/2;
        appOne = one + Sep;
        if(abs(appOne - one) == 0.0){
            break;
        }
        
    }
    std::cout << "Digits: " << iPow << " Machine Ep: " << Sep << endl;
}
```

