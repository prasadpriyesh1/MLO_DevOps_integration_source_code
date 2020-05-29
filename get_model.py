# -*- coding: utf-8 -*-
"""
Created on Mon May 18 12:21:44 2020

@author: prasa
"""

from keras.models import load_model
import pickle
try:
    model = load_model("mymodel.h5")
    s = model.layers[0].__class__.__name__
    file = open("model.txt","w+")
    if (s == "Dense"):
        file.write("ANN")
    else:
        file.write("CNN")
    file.close()
except:
    pickle.load(open("mymodel.h5","rb"))
    file = open("model.txt","w+")
    file.write("SKLEARN")
    file.close()

        