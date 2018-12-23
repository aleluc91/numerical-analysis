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

def mean(x):
    return sum(x) / len(x)

def variance(x):
    tmp = []
    m = mean(x)
    for i in range(0, len(x)):
        value = x[i] - m
        tmp.append(value ** 2)
    return sum(tmp) / len(x)
    

x = [1.5, -0.2, -3.1, 2.6]
s_result = sum(x)
m_result = mean(x)
v_result = variance(x)

x = np.array([1.5, -0.2, -3.1, 2.6])
s_result = sum(x)
m_result = mean(x)
v_result = variance(x)

x = np.array([1.5, -0.2, -3.1, 2.6])
s_result = np.sum(x)
m_result = np.mean(x)
v_result = np.var(x)