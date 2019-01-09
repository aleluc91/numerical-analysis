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

test_mat_3 = np.array([[1., 1., 1.], [2., 3., 4.], [4., 9., 16.]])
test_mat_v_3 = np.array([1., 3., 11.])



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

def gauss_no_pivoting(A, b):
    m, n = A.shape
    mat = np.copy(A)
    vet = np.copy(b)
    for i in range(0, n):
        if mat[i][i] == 0:
            for j in range(i+1, n):
                if mat[j][i] != 0:
                    swap(mat, vet, i, j)  
                    break
        else:
           for j in range(i+1, n):
               if mat[j][i] != 0:
                   m = mat[j][i]/mat[i][i]
                   for k in range(0, n):
                       mat[j][k] -= mat[i][k] * m
                   vet[j] -= vet[i] * m
    return mat, vet

def gauss_partial_pivoting(A, b):
    m, n = A.shape
    mat = np.copy(A)
    vet = np.copy(b)
    for i in range(0, n):
        max_row = find_max_row(mat, i)
        if max_row != i:
            swap(mat, vet, i, max_row)
        for j in range(i+1, n):
            if mat[j][i] != 0:
                m = mat[j][i]/mat[i][i]
                for k in range(0, n):
                    mat[j][k] -= mat[i][k] * m
                vet[j] -= vet[i] * m
    return mat, vet
                  

def swap(A, b, i, j):
    m, n = A.shape
    for k in range(i, n):
        temp = A[j][k]
        A[j][k] = A[i][k]
        A[i][k] = temp
    temp = b[j]
    b[j] = b[i]
    b[i] = temp

def find_max_row(A, i):
    m, n = A.shape
    max_elem = np.abs(A[i][i])
    max_row = i
    for j in range(i+1, n):
        if np.abs(A[j][i]) > max_elem:
            max_elem = np.abs(A[j][i])
            max_row = j
    return max_row
    
