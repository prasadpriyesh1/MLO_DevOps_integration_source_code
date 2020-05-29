# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:49:23 2020

@author: prasa
"""
from keras.models import Model
from keras.layers import Dense
from keras.models import save_model
from keras.models import Sequential
from keras.utils.np_utils import to_categorical
from keras.optimizers import Adam
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
class CNN:
    model = ""
    model2 = ""
    def __init__ (self,model):
        self.model = model 
    def change_model(self):
        n=0
        n2 = len(self.model.layers)
        for x in self.model.layers:
            if x.__class__.__name__ == "Dense":
                n +=1
        if n <=6:
            self.model2 = Sequential()
            self.model2.add(Conv2D(filters=32, 
                        kernel_size=(3,3), 
                        activation='relu',
                   input_shape=(28,28,1)
                       ))
            self.model2.add(MaxPooling2D(pool_size=(2, 2)))
            self.model2.add(Conv2D(filters=32, 
                        kernel_size=(3,3), 
                        activation='relu',
                       ))
            self.model2.add(MaxPooling2D(pool_size=(2, 2)))
            self.model2.add(Flatten())
            for x in range(n2-n,n2-1):
                if x == (n2-2):
                    p = self.model.layers[x].units * (2**(x - (n2-n)))
                    if p == 256 and (self.model.layers[x].units/2 >10):
                        if x ==  n2-n:
                            self.model2.add(Dense(units = 256,input_dim =28*28,activation = "relu" ))
                        else:
                            self.model2.add(Dense(units = self.model.layers[x].units,activation = "relu" ))
                        self.model2.add(Dense(units = 8,activation ="relu"))
                    elif p<256:
                        k = self.model.layers[x].units + 8
                        if x ==  n2-n:
                            self.model2.add(Dense(units = k,input_dim =28*28,activation = "relu" ))
                        else:
                            self.model2.add(Dense(units = k,activation = "relu" ))
                    else:
                        self.model2.add(Dense(units = 16, activation = "relu"))
                else:
                    k = self.model.layers[x].units
                    if x ==  n2-n:
                        self.model2.add(Dense(units = k,input_dim =28*28,activation = "relu" ))
                    else:
                        self.model2.add(Dense(units = k,activation = "relu" ))
            self.model2.add(Dense(units = 10 , activation = 'softmax'))
            self.model2.summary()
            self.model2.compile(optimizer = Adam(), loss = 'categorical_crossentropy', metrics = ['accuracy'])
            return self.model2
        else:
            return self.model
        
#    def save_model_f(self):
 #       save_model(self.model2, "mymodel.h5",overwrite = True)