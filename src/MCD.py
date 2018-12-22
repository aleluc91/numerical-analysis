#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 18:47:07 2018

@author: aleluc
"""

def MCD_recursive(m, n):
    if m > n:
        return MCD_recursive(m-n , n)
    elif n > m:
        return MCD_recursive(m, n-m)
    else:
        return m
    
def MCD(m, n):
    while m != n:
        if m > n:
            m = m - n
        elif n > m:
            n = n - m
    return m
    
print(MCD_recursive(30 , 18))
print(MCD(30 , 18))