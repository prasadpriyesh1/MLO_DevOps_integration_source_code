# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:31:25 2020

@author: prasa
"""
from keras.datasets import fashion_mnist
from keras.models import save_model
import numpy as np
# In[2]:


dataset = fashion_mnist.load_data()


# In[3]:


train , test = dataset


# In[4]:


x_train , y_train = train
x_test , y_test = test
x_train = np.expand_dims(x_train, -1)

# In[5]:


#x_train_1D = x_train.reshape(-1 , 28*28)
#x_test_1D = x_test.reshape(-1 , 28*28)


# In[6]:


#x_train = x_train_1D.astype('float32')
#x_test = x_test_1D.astype('float32')


# In[7]:


from keras.utils.np_utils import to_categorical
from keras.optimizers import Adam

# In[8]:


y_train = to_categorical(y_train)
#y_test = to_categorical(y_test)


# In[16]:



try:
    from keras.models import load_model
    
    model = load_model("mymodel.h5")
    print("model loaded")
    #model.compile(optimizer = Adam(), loss = 'categorical_crossentropy', metrics = ['accuracy'])
    model.fit(x_train , y_train , epochs= 10)
    file2 = open("accuracy.txt","w+")
    x = str(model.evaluate(x_train,y_train)[1])
    print(x)
    file2.write(x)
    file2.close()
    save_model(model, "mymodel.h5",overwrite = True)
except:

    from keras.layers import Conv2D
    from keras.layers import MaxPooling2D
    from keras.layers import Flatten
    from keras.layers import Dense
    from keras.models import Sequential
    model = Sequential()
    model.add(Conv2D(filters=32, 
                        kernel_size=(3,3), 
                        activation='relu',
                   input_shape=(28,28,1)
                       ))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(filters=32, 
                        kernel_size=(3,3), 
                        activation='relu',
                       ))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(units=8, activation='relu',name = "layer1"))
    model.add(Dense(units = 10 , activation = 'softmax'))
    model.summary()
    model.compile(optimizer = Adam(), loss = 'categorical_crossentropy', metrics = ['accuracy'])
    model.fit(x_train , y_train , epochs= 10)
    file2 = open("accuracy.txt","w+")
    x = str(model.evaluate(x_train,y_train)[1])
    print(x)
    file2.write(x)
    file2.close()
    save_model(model, "mymodel.h5",overwrite = True)