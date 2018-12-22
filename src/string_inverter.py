#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 16:12:23 2018

@author: aleluc
"""

def invert_string(input_string):
    output_string = ""
    for i in range(len(input_string) - 1, -1, -1):
        output_string += input_string[i]
    return output_string


s = "acetone"
print(invert_string(s))
