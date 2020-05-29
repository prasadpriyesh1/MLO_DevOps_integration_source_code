#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

import pickle
# In[4]:


dataset = pd.read_csv("Social_Network_Ads.csv")


# In[5]:


X = dataset[['Age', 'EstimatedSalary' ] ]
y = dataset['Purchased']


# In[6]:


from sklearn.model_selection import train_test_split


# In[7]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)


# In[8]:

try:
    
    model = pickle.load(open("mymodel.h5","rb"))
    print("model loaded")
    #model.compile(optimizer = Adam(), loss = 'categorical_crossentropy', metrics = ['accuracy'])
    model.fit(X_train , y_train )
    
    file2 = open("accuracy.txt","w+")
    
    #x = str(model.evaluate(x_train,y_train)[1])
    x =str( model.score(X_test,y_test))
    print(x)
    
    file2.write(x)
    
    file2.close()
    pickle.dump(model, open("mymodel.h5","wb"))
except:
    from sklearn.neighbors import KNeighborsClassifier
    
    
    # In[9]:
    
    
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(X_train, y_train)
    
    
    
    # In[13]:
    
    
   
    
    
    # In[14]:
    
    
    pickle.dump(model, open("mymodel.h5","wb"))


# In[ ]:




