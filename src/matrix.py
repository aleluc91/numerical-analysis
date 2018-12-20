# -*- coding: utf-8 -*-
"""
Spyder Editor

@author Alessio Lucarella
"""

import random

class Matrix:
    
    def __init__(self, n, m, gen = "random"):
        self.matrix = []
        self.n = n
        self.m = m
        for i in range(0, n):
            if gen == "random":
                self.matrix.append(self.__generate_rows_of_rand_number(m))
            elif gen == "zeros":
                self.matrix.append(self.__generate_rows_of_zeros(m))
            
    def __generate_rows_of_zeros(self, m):
        row = []
        for i in range(0, m):
            row.append(0)
        return row
    
    def __generate_rows_of_rand_number(self, m):
        row = []
        for i in range(0, m):
            row.append(random.randrange(0, 100))
        return row
    
    def __str__(self):
        result = ""
        for i in range(0, self.n):
            result += "["
            for j in range(0, self.m):
                result += str(self.matrix[i][j])
                if j != self.m - 1:
                    result += " "
            result += "]\n"
        return result
    
    
matrix = Matrix(2, 2)
print(matrix)
