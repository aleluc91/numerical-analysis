#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:19:48 2019

@author: aleluc
"""

import numpy as np

rand_mat = np.random.randint(10, size = (3, 3))
rand_vector = np.random.randint(5, size = 3)
rand_mat_triu = np.triu(rand_mat)
rand_mat_tril = np.tril(rand_mat)

test_mat = np.array([[1, 1, -2], [1, -1, 1], [2, 0, -1]])
test_mat_v = np.array([0, 1, 0])

test_mat_2 = np.array([[1, 1, -2], [1, -1, 1], [2, 0, -1]])
test_mat_v_2 = np.array([0, 1, 1])



def back_substitution(A, b):
    m, n = A.shape
    x = np.zeros(n)
    #x[n-1] = b[n-1] / A[n-1][n-1] 
    for i in range(n-1, -1, -1):
        if np.abs(A[i][i]) < 1e-15:
            return "Singular matrix"
        values_sum = np.sum([A[i][j] * x[j] for j in range(i, n)])
        x[i] = (b[i] - values_sum) / A[i][i]
    return x

def forward_substitution(A, b):
    m, n = A.shape
    x = np.zeros(n)
    x[0] = b[0] / A[0][0] 
    for i in range(0, n):
        if np.abs(A[i][i]) < 1e-15:
            return "Singular matrix"
        values_sum = np.sum([A[i][j] * x[j] for j in range(0, i)])
        x[i] = (b[i] - values_sum) / A[i][i]
    return x

def gaussian_elimination(A, b):
    m, n = A.shape
    for i in range(0, n):
        if A[i][i] == 0:
            for j in range(i+1, n):
                if A[j][i] != 0:
                    A, b = swap(A, b, i, j)  
                    break
        else:
           for j in range(i+1, n):
               if A[j][i] != 0:
                   m = A[j][i]/A[i][i]
                   for k in range(0, n):
                       A[j][k] -= A[i][k] * m
                   b[j] -= b[i] * m
    return A, b
        

def swap(A, b, i, j):
    m, n = A.shape
    for k in range(i, n):
        temp = A[j][k]
        A[j][k] = A[i][k]
        A[i][k] = temp
    temp = b[j]
    b[j] = b[i]
    b[i] = temp
    return A, b