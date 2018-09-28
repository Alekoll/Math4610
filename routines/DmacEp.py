#!/usr/bin/env python3

import cmath

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

    return Dep

