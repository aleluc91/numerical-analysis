#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 17:52:44 2019

@author: aleluc
"""

import numpy as np
import random

mat = np.array([[1, 1, 1], [2, -1, 1], [1, 0 ,0]])
mat1 = np.matrix("1 2; 3 4")
mat2 = np.array([[1., 2., 1., 1.], [2., 1., 3., 1.], [0., 2., 2., 0.], [1., 2., 0., 0.]])


def det(A):
    m, n = np.shape(A)
    if m == n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    elif m == n == 3:
        return sarrus(A)
    elif m == n >= 4:
        return det_lagrange(A)
    else:
        return None
    
def det_lagrange(A):
    print(A)
    m, n = np.shape(A)
    #TODO Sistemare il caso in cui entrambi siano nulli
    if m == n == 2:
        print(det1(A))
        return det1(A)
    best_row = find_laplace_best_row(A)
    best_column = find_laplace_best_column(A)
    det_value = 0
    if best_row[0] != -1 or best_column[0] != -1:
        if best_row[1] >= best_column[1]:
            print("row")
            #loop for row
            for k in range(0, n):
                print(A[best_row[0]][k])
                det_value += ((-1) ** (best_row[0] + k)) * A[best_row[0]][k] * det_lagrange(clean_matrix(A, best_row[0], k))
                #if m == n == 3:
                    #det_value += (-1 ** (best_row[0] + k)) * A[best_row[0]][k] * det_lagrange(clean_matrix(A, best_row[0], k))
                #else:
                    #det_value += (-1 ** (best_row[0] + k)) * A[best_row[0]][k] * det_lagrange(clean_matrix(A, best_row[0], k))
        else:
            #loop for column
            print("column")
            for k in range(0, m):
                print(A[k][best_column[0]])
                det_value += ((-1) ** (best_column[0] + k)) * A[k][best_column[0]] * det_lagrange(clean_matrix(A, k, best_column[0]))
                #if m == n == 3:
                    #det_value += (-1 ** (best_column[0] + k)) * A[k][best_column[0]] * det_lagrange(clean_matrix(A, k, best_column[0]))
                #else:
                    #det_value += (-1 ** (best_column[0] + k)) * A[k][best_column[0]] * det_lagrange(clean_matrix(A, k, best_column[0]))
    else:
        #if no starting row or column has benn found, choose a random row or column in the range values of the matrix
        choice = random.randint(0,1)
        if choice == 0:
            rand_row = random.randint(0, m - 1)
            for k in range(0, n):
                det_value += ((-1) ** (rand_row + k)) * A[rand_row][k] * det_lagrange(clean_matrix(A, rand_row, k))
        else:
            rand_column = random.randint(0, n - 1)
            for k in range(0, m):
                det_value += ((-1) ** (rand_column + k)) * A[k][rand_column] * det_lagrange(clean_matrix(A, k, rand_column))
    return det_value
        

def det1(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]

def clean_matrix(A, row_number, column_number):
    m, n = np.shape(A)
    temp_matrix = []
    for i in range(0, m):
        if i != row_number:
            temp_row = []
            for j in range(0, n):
                if j != column_number:
                    temp_row.append(A[i][j])
            temp_matrix.append(temp_row)
    return np.array(temp_matrix)
                
def sarrus(A):
    v1 = A[0][0] * A[1][1] * A[2][2]
    v2 = A[0][1] * A[1][2] * A[2][0]
    v3 = A[0][2] * A[1][0] * A[2][1]
    v4 = A[2][0] * A[1][1] * A[0][2]
    v5 = A[2][1] * A[1][2] * A[0][0]
    v6 = A[2][2] * A[1][0] * A[0][2]
    return v1 + v2 + v3 - v4 - v5 - v6

def find_laplace_best_row(A):
    m, n = np.shape(A)
    row , zeros_count = None, 0
    for i in range(0, m):
        temp_count = 0
        for j in range(0, n):
            if A[i][j] == 0:
                temp_count += 1
        if temp_count > zeros_count:
            row, zeros_count = i, temp_count
    if zeros_count != 0:
        return row, zeros_count
    else:
        return (-1, -1)
    
def find_laplace_best_column(A):
    m, n = np.shape(A)
    row , zeros_count = None, 0
    for i in range(0, n):
        temp_count = 0
        for j in range(0, m):
            if A[j][i] == 0:
                temp_count += 1
        if temp_count > zeros_count:
            row, zeros_count = i, temp_count
    if zeros_count != 0:
        return row, zeros_count
    else:
        return (-1 , -1)
    
    
    