# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:29:56 2020

@author: prasa
"""
from ANN_modify import ANN
from CNN_modify import CNN
from sklearn_modify import SKLEARN
from keras.models import load_model
#from keras.datasets import fashion_mnist
from keras.models import save_model

# In[2]:


#dataset = fashion_mnist.load_data()


# In[3]:


#train , test = dataset


# In[4]:


#x_train , y_train = train
#x_test , y_test = test


# In[5]:


#x_test_1D = x_test.reshape(-1 , 28*28)


# In[6]:


#x_train = x_train_1D.astype('float32')
#x_test = x_test_1D.astype('float32')


# In[7]:


import pickle

# In[8]:


#y_train = to_categorical(y_train)

file = open("model.txt","r")
if file.readline() == "ANN":
    model = load_model("mymodel.h5")
    code = ANN(model)
    new_model = code.change_model()

    save_model(new_model, "mymodel.h5",overwrite = True)
file.close()
file = open("model.txt","r")
if file.readline() == "CNN":
    model = load_model("mymodel.h5")
    code = CNN(model)
    new_model = code.change_model()

    save_model(new_model, "mymodel.h5",overwrite = True)
file.close()
file = open("model.txt","r")
if file.readline() == "SKLEARN":
    model = pickle.load(open("mymodel.h5","rb"))
    code = SKLEARN(model)
    new_model = code.change_model()
    pickle.dump(new_model , open("mymodel.h5","wb"))
file.close()



#new_model.fit(x_train , y_train , epochs= 20)
#save_model(new_model, "mymodel.h5",overwrite = True)