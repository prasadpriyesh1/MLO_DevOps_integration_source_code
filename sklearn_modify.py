# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:49:59 2020

@author: prasa
"""

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
class SKLEARN:
    model = ""
    model2 = ""
    def __init__ (self,model):
        self.model = model 
    def change_model(self):
        if self.model.__class__.__name__ =="KNeighborsClassifier":
            self.model2 = self.KNN()
            return self.model2
    def KNN(self):
        n = self.model.n_neighbors
        if n < 15:
            n += 1
            model = KNeighborsClassifier(n_neighbors = n)
            
            return model
    def save_model_f(self):
        pass