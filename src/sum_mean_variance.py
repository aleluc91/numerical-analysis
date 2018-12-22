#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 19:17:58 2018

@author: aleluc
"""

import numpy as np

def sum(x):
    sum = 0
    for i in range(0, len(x)):
       sum += x[i]
    return sum

x = [1.5, -0.2, -3.1, 2.6]
result = sum(x)

x = np.array([1.5, -0.2, -3.1, 2.6])
result = sum(x)

x = np.array([1.5, -0.2, -3.1, 2.6])
result = np.sum(x)