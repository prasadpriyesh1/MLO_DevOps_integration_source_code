# -*- coding: utf-8 -*-
"""
Created on Thu May 21 11:46:16 2020

@author: prasa
"""
from sys import exit
file = open("accuracy.txt")
str = file.readline()
n = float(str)

if n >= 0.85:
    print("greater")
    exit(1)
else:
    print("less")
    exit(0)