#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 12:09:59 2018

@author: aleluc
"""

import csv
from matplotlib import pyplot as plt
#import numpy as np
#import pandas
#import os

def read_csv(f, column_name = None):
    rows = {}
    with open(f, newline = '')  as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        if column_name != None:
            columns = find_index(next(csv_reader), column_name)
        for row in csv_reader:
            for i in range(0, len(row)):
                if i in columns:
                    current_tuple = columns.get(i)
                    current_tuple[1].append(float(row[i]))
    for i in range(0, len(columns)):
        rows[columns.get(i)[0]] = columns.get(i)[1]
    return rows

def find_index(data, column_name):
    columns = {}
    for i in range(0, len(column_name)):
        for j in range(0, len(data)):
            if data[j] == column_name[i]:
                columns[j] = (data[j] , [])
    return columns

def sum(data):
    value = 0
    for i in range(0, len(data)):
        value += data[i]
    return value

def mean_value(data):
    s = sum(data)
    if sum != None:
        return (1 / (len(data))) * s
        #return (1 / ((len(data) - 1) + 1)) * s
    else:
        raise ValueError
        
def covariance(x_data, y_data):
    x_mean = mean_value(x_data)
    y_mean = mean_value(y_data)
    value = 0
    for i in range(0, len(x_data)):
        value += (x_data[i] - x_mean) * (y_data[i] - y_mean)
    return (1 / (len(x_data) - 1)) * value
    #return (1 / ((len(data) - 1) + 1)) * value

def variance(x_data):
    x_mean = mean_value(x_data)
    value = 0
    for i in range(0, len(x_data)):
        value += (x_data[i] - x_mean) ** 2
    return (1 / (len(x_data) - 1)) * value
    #return (1 / ((len(data) - 1) + 1)) * value
    
def linear_regression(x_data, a0, a1):
    regression_value = []
    for i in range(0, len(x_data)):
        regression_value.append((a0 * x_data[i]) + a1)
    return regression_value
    

data = read_csv("/home/aleluc/Desktop/Programming/numerical-analysis/src/test1.csv", column_name = ["x", "y"])
covar = covariance(data["x"], data["y"])
variance = variance(data["x"])
a0 = covar/variance
a1 = mean_value(data["y"]) - (a0 * mean_value(data["x"]))
plt.scatter(data["x"], data["y"], color = "red")
plt.plot(data["x"], linear_regression(data["x"], a0, a1), color = "black", linewidth = 1)
#data = pandas.read_csv("/home/aleluc/Desktop/Programming/numerical-analysis/src/test1.csv")

            