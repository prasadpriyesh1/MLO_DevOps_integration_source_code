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
        n = len(self.model.layers)
        if self.model.layers[-2].units * (2**(n-2)) == 256:
            if 256 / (2**(n-1)) >10:
                a = self.model.get_layer("layer"+str(n-1))
                s = "layer"+str(n)
                x = Dense(8 , activation ="relu", name = s)(a)
                
                x = Dense(10, activation ="softmax")(a)
                self.model2 = Model(input = self.model.input, outputs = x)
        else:
            n1 = self.model.layers[-2].units
            if n == 2:
                
                
                n3= n1 + 8
                s = "layer1"
                x = Sequential()
                x.add(Dense(n3 ,input_dim =28*28,  activation = "relu",name = s))
                x.add(Dense(10, activation ="softmax"))
                self.model2 = x 
            else:
                s = "layer"+str(n-1)
                a = self.model.get_layer(s)
                n3 = n1 + 8
                x = Dense(n3 , activation = "relu",name = s)(a)
                x = Dense(10, activation ="softmax")(a)
                self.model2 = Model(input = self.model.input, outputs = x)
        return self.model2
        
#    def save_model_f(self):
 #       save_model(self.model2, "mymodel.h5",overwrite = True)