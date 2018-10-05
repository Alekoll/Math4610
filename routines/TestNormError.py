#!/usr/bin/env python3

import VectorErrors

#Test the relative and absolute error on the norms of given vectos

def VectorErrorsTest():
    Exact = [1,2,3,4,5,6,7,8,9]
    Approx = [.987654,1.98888,2.988878, 3.9999857, 4.985443, 5.97979, 6.989978544, 7.9987, 8.998766]

    absNorm1 = VectorErrors.AbsErrorLengthNorm1(Approx, Exact)
    relNorm1 = VectorErrors.RelErrorLengthNorm1(Approx, Exact)

    absNorm2 = VectorErrors.AbsErrorLengthNorm2(Approx, Exact)
    relNorm2 = VectorErrors.RelErrorLengthNorm2(Approx, Exact)

    absNormInf = VectorErrors.AbsErrorLengthNormInf(Approx, Exact)
    relNormInf = VectorErrors.AbsErrorLengthNormInf(Approx, Exact)
    
    print(absNorm1, absNorm2, absNormInf, sep='\n')
    print(relNorm1, relNorm2, relNormInf, sep='\n')
    

    
