#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 12:09:59 2018

@author: aleluc
"""

import csv
#import pandas
#import os

def read_csv(f):
    rows = []
    with open(f, newline = '')  as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            rows.append(row)
    return rows

print(read_csv("/home/aleluc/Desktop/Programming/numerical-analysis/src/test1.csv"))

#data = pandas.read_csv("/home/aleluc/Desktop/Programming/numerical-analysis/src/test1.csv")

            