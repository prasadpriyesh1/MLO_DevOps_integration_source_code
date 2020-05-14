# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:55:58 2020

@author: prasa
"""
import os
file1 = open("main_accuracy.txt","r")
file2 = open("test_accuracy.txt","r")
if file1.readline():
    a = True
else:
    a = False
file1.close()

#print (float(file2.readline()))
a2 = float(file2.readline())
if not a:
    file1 = open("main_accuracy.txt","w")
    
    file1.write(str(a2))
    file1.close()
    print(2)
else:
    file1 = open("main_accuracy.txt","r")
    a1 = float(file1.readline())
    file1.close()
    
    if a1<a2:
        file1 = open("main_accuracy.txt","w")
        file1.write(str(a2))
        file1.close()


file2.close()