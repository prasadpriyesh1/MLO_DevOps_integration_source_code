# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:29:56 2020

@author: prasa
"""
from ANN_modify import ANN
from CNN_modify import CNN
from sklearn_modify import SKLEARN
from keras.models import load_model
from keras.datasets import fashion_mnist
from keras.models import save_model

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

# In[8]:


y_train = to_categorical(y_train)
model = load_model("mymodel.h5")
file = open("model.txt","r")
if file.readline() == "ANN":
    code = ANN(model)
file.close()
file = open("model.txt","r")
if file.readline() == "CNN":
    code = CNN(model)
file.close()
file = open("model.txt","r")
if file.readline() == "SKLEARN":
    code = SKLEARN(model)
file.close()
new_model = code.change_model()
new_model.compile(optimizer = Adam(), loss = 'categorical_crossentropy', metrics = ['accuracy'])
new_model.fit(x_train , y_train , epochs= 20)
save_model(new_model, "mymodel.h5",overwrite = True)