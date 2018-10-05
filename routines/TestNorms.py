#!/usr/bin/env python3

import lengthnorms


#this program is created to test the norms

def testNorms():

    testList = [3,54,656,43,23,64,76,32,1,25,45.232,4565.7685,674.9876]

    length1 = lengthnorms.LengthNorm1(testList)
    length2 = lengthnorms.LengthNorm2(testList)
    lengthinf = lengthnorms.LengthNormInf(testList)

    print(length1,length2, lengthinf, sep='\n')
    

testNorms()
