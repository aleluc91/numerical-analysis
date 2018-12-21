#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:22:24 2018

@author: aleluc
"""

import numpy as np

def eq2(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        return False
    else:
        x1 = (-b + np.sqrt(d)) / (2 * a)
        x2 = (-b - np.sqrt(d)) / (2 * a)
    return [x1, x2]

def delta(a, b, c):
    return b ** 2 - 4 * a * c


a = 1
b = -5
c = 6
result = eq2(a, b, c)
