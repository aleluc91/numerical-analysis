#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 20:37:36 2018

@author: aleluc
"""

import numpy as np

def collatz(x):
    sequence = []
    while x != 1:
        if x % 2 == 0:
            value = x / 2
            sequence.append(value)
            x = value
        else:
            value = 3 * x + 1
            sequence.append(value)
            x = value
    return sequence

def collatz_np(x):
    sequence = []
    while x != 1:
        if np.mod(x, 2) == 0:
            value = x / 2
            sequence.append(value)
            x = value
        else:
            value = 3 * x + 1
            sequence.append(value)
            x = value
    return sequence

def collatz_recursive(x, sequence):
    if x == 1:
        return sequence
    elif x % 2 == 0:
        value = x / 2
        sequence.append(value)
        return collatz_recursive(value, sequence)
    else:
        value = 3 * x + 1
        sequence.append(value)
        return collatz_recursive(value, sequence)
    
def collatz_recursive_np(x, sequence):
    if x == 1:
        return sequence
    elif np.mod(x, 2) == 0:
        value = x / 2
        sequence.append(value)
        return collatz_recursive_np(value, sequence)
    else:
        value = 3 * x + 1
        sequence.append(value)
        return collatz_recursive_np(value, sequence)
    
result1 = collatz(27)
result2 = collatz_np(27)
result3 = collatz_recursive(27, [])
result4 = collatz_recursive_np(27, [])