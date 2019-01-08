#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 17:08:35 2019

@author: aleluc
"""

import numpy as np

def cofactor(A, i, j):
    m, n = A.shape
    if m != n: 
        raise ValueError()
    A1 = np.delete(A, i, axis = 0)
    A1 = np.delete(A1, j, axis = 1)
    minor = np.linalg.det(A1)
    return ((-1) ** (i + j)) * minor

def cofactor_expansion(A):
    m, n = A.shape
    if m != n:
        raise ValueError()
    a = A[:1].flatten()
    cof = []
    for i in range(0, m):
        c = cofactor(A, 0, i)
        cof.append(c)
    c = np.array(c)
    return np.sum(np.multiply(a, cof))

def adjoint(A):
    m, n = A.shape
    if m != n:
        raise ValueError()
    A1 = []
    for i in range(0, n):
        for j in range(0, n):
            A1.append(cofactor(A, i, j))
    A1 = np.array(A1)
    return A1.reshape((m, n)).T

def inverse(A):
    adj = adjoint(A)
    det = cofactor_expansion(A)
    return (1/det) * adj
    
    

mat = np.array([[2, 3 ,-1], [5, 3, 2], [4, -2, 4]])
mat1 = np.array([[3, 1 ,-4], [2, 5, 6], [1, 4, 8]])
mat2 = np.array([[1., 2., 1., 1.], [2., 1., 3., 1.], [0., 2., 2., 0.], [1., 2., 0., 0.]])
mat3 = np.array([[1, 2, -1], [2, -1, 1], [1, 2, 2]])
mat4 = np.array([[1, -1, 1, 2], [1, 0, 1, 3], [0, 0, 2, 4], [1, 1, -1, 1]])
