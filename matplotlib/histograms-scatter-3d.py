#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# histograms ________________


# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:


# random data 

a = np.random.randn(1000)


# In[ ]:


# so the basic function to plot histogram is plt.hist()

plt.hist(a,10,color = "darkcyan")

plt.show()

# the second parameter is frequency of plots per width 


# In[ ]:


# Scatter plot ______________


# In[ ]:


#random data 

a = np.random.randn(100)
b = np.random.randn(100)

plt.scatter(a,b)
plt.title("SCATTER-PLOT-EXAMPLE")
plt.xlabel("random -a")
plt.ylabel("random -b")
plt.show()


# In[ ]:


#3d plots 


# In[ ]:


# we have to import mplot3d  from mpl_toolkits package 

from mpl_toolkits import mplot3d


# In[ ]:


c = plt.axes(projection = "3d")

c.scatter3D(a,b)
plt.show()


# In[ ]:




