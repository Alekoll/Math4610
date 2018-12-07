#!/usr/bin/env python3

def Frobenius(matrix):
    row = len(matrix)
    col = len(matrix[0])
    norm = 0.0

    for i in range(row):
        for j in range(col):
            norm += abs(matrix[i][j] * matrix[i][j])
    norm = norm**(.5)

    return norm

def OneNorm(matrix):
    row = len(matrix)
    col = len(matrix[0])
    norm = 0.0
    colSum = []

    for j in range(col):
        for i in range(row):
            norm += abs(matrix[i][j])
        colSum.append(norm)
        norm = 0.0
    
    norm = max(colSum)
    return norm

def InfNorm(matrix):
    row = len(matrix)
    col = len(matrix[0])
    norm = 0.0
    rowSum = []

    for i in range(row):
        for j in range(col):
            norm += abs(matrix[i][j])
        rowSum.append(norm)
        norm = 0.0
    
    norm = max(rowSum)
    return norm


