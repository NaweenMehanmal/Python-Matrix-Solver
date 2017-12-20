# Filename: matrix.py
# Assignment: Programming Assignment 1 - MATH3160
# By: Naween Mehanmal
# Date: December 18, 2017
# Description: Program that solves matrix for N unknowns and also 
# calculates the inverse if requested
import sys
import numpy as np

# [A][X] = [B]
#
# 0,1,2;1,0,3;4,5,6 -> 3x3 Matrix
#
# Condition as second argument
cond = sys.argv[1]

if cond == "solve": 
    preA = input('Enter coefficient matrix: ')
    preB = input('Enter value matrix: ')
    A = np.matrix(preA) #Coefficient matrix
    B = np.matrix(preB) #Value matrix 
    X = np.linalg.solve(A, B)
    print('Inverse of Matrix A is:\n\n', np.around(X, decimals=5))
    #print('Inverse of Matrix A is:\n\n', X)

elif cond == "inverse":
    preA = input('Enter original matrix: ')
    A = np.matrix(preA)
    inverse = np.linalg.inv(A)
    print('Inverse of Matrix A is:\n\n', inverse)

else:
    print('Arguments not recognized')
