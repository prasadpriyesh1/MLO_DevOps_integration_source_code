# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:45:25 2020

@author: prasa
"""
from keras.models import Model
from keras.layers import Dense
from keras.models import save_model
from keras.datasets import fashion_mnist

from keras.models import Sequential
# In[2]:


dataset = fashion_mnist.load_data()


# In[3]:


train , test = dataset


# In[4]:


x_train , y_train = train
x_test , y_test = test


# In[5]:


x_train_1D = x_train.reshape(-1 , 28*28)
x_test_1D = x_test.reshape(-1 , 28*28)


# In[6]:


x_train = x_train_1D.astype('float32')
x_test = x_test_1D.astype('float32')


# In[7]:


from keras.utils.np_utils import to_categorical
from keras.optimizers import Adam
class ANN:
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