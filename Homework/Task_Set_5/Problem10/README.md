# Compare the different methods.

## Description
The goal is to compare the results of different randomsized matrices the different algorithm. We are using two types of Measurements. 
The first measurement is how long did the process take. Using time.proccess_time(), we were able to time each one. Next is the absolute error of the norm2.

## Results

### (40 X 40)

Jacobi Time:  0.0026770000000000058

GaussSeidel Time: 0.003804000000000002

Steepest:  0.06576299999999999

Conjugate:  0.12576700000000002

Error: [7.275957614183426e-12, 7.275957614183426e-12, 2.7894129743799567e-05, 7.275957614183426e-12]

### (80 X 80)

Jacobi Time:  0.010216999999999976

GaussSeidel Time: 0.013246999999999981

Steepest:  0.19549999999999998

Conjugate:  0.403213

Error: [5.820766091346741e-11, 5.820766091346741e-11, 6.512564141303301e-06, 5.820766091346741e-11]

### (160 X 160)

Jacobi Time:  0.04092999999999991

GaussSeidel Time: 0.05213699999999988

Steepest:  0.5339170000000002

Conjugate:  1.03206

Error: [1.1641532182693481e-10, 1.1641532182693481e-10, 2.0189909264445305e-06, 1.1641532182693481e-10]

### (320 X 320)

Jacobi Time:  0.16770899999999855

GaussSeidel Time: 0.2158010000000008

Steepest:  1.975855000000001

Conjugate:  4.082512999999999

Error: [0.0, 0.0, 1.728767529129982e-07, 1.1641532182693481e-10]

### (640 X 640)

Jacobi Time:  0.7047129999999981

GaussSeidel Time: 0.858167999999992

Steepest:  6.365458000000004

Conjugate:  13.065046999999993

Error: [2.3283064365386963e-10, 2.3283064365386963e-10, 2.2025778889656067e-07, 2.3283064365386963e-10]

### Conclusion

The Gradient methods take much longer than Jacobi and Gauss, but that could be that my functions are ill-conditioned.

![](https://github.com/Alekoll/Math4610/blob/master/Homework/Task_Set_5/Problem10/DifferentIterative.pdf)








