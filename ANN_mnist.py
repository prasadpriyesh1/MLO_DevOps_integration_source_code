#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.datasets import mnist


# In[2]:


dataset = mnist.load_data('mymnist.db')


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


# In[8]:


y_train = to_categorical(y_train)
#y_test = to_categorical(y_test)


# In[9]:


from keras.models import Sequential
from keras.layers import Dense


# In[10]:


model = Sequential()


# In[11]:


model.add(Dense(units = 512,input_dim = 28*28 ,activation = 'relu'))
model.add(Dense(units = 256, activation = 'relu'))
model.add(Dense(units = 128, activation = 'relu'))
model.add(Dense(units = 32, activation = 'relu'))


# In[12]:


model.summary()


# In[13]:


model.add(Dense(units = 10 , activation = 'softmax'))


# In[14]:


model.summary()


# In[15]:


from keras.optimizers import Adam


# In[16]:


model.compile(optimizer = Adam(), loss = 'categorical_crossentropy', metrics = ['accuracy'])


# In[17]:


model.fit(x_train , y_train , epochs= 20)
print(model.evaluate(x_train,y_train)[1])


# In[18]:



#t1 = model.predict_classes(x_test)


# In[19]:


#from sklearn.metrics import confusion_matrix


# In[20]:


#t1.shape
#y_test.shape


# In[21]:


#confusion_matrix(y_test , t1)


# In[ ]:




