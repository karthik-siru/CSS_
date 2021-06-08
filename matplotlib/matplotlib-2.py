#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:


month = ['jan','feb','mar','apr','may']

city1_sales = [50,60,49,67,26]
city2_sales = [65,78,98,8,45]


# In[ ]:


# BARPLOTS - HISTOGRAMS - PIE CHARTS - SCATTERPLOTS - 3DPLOTS


#-----------------------BARPLOTS---------------------------

plt.bar(month , city1_sales ,color = "yellow")
plt.xlabel(" months ")
plt.ylabel(" Sales  ")
plt.show()

# pretty cool (weird i know ) right ?????


'''
  But there is one problem , what if i draw another bar plot of city2_sales just after the city1_plot ??
'''
plt.bar(month , city1_sales ,color = "yellow")
plt.bar(month , city2_sales , color = "blue")
plt.title("combined bar graph :(")
plt.xlabel("months")
plt.ylabel("sales")
plt.show()

# Let's tackle this  --- ofcourse , you can do this by simply plt.show() in b/w 

index = np.arange(1,6)

width = 0.30

plt.bar(index , city1_sales , width , color  = "green" , label = "City1_sales")
plt.bar(index+width , city2_sales , width , color  = "red" , label = "City2_sales")

plt.title("HORIZANTALLY STACKED BARGRAPH")
plt.xlabel(" months ")
plt.ylabel(" Sales  ")

plt.legend(loc = "best") # we can explicitly give the location of legend or , we can simply best-which will automatically fits the best
plt.show()


#let's do the horizantal one 

plt.barh(index , city1_sales , width , color  = "green" , label = "City1_sales")
plt.barh(index+width , city2_sales , width , color  = "red" , label = "City2_sales")

plt.title("VERTICALLY STACKED BARGRAPH")
plt.xlabel(" months ")
plt.ylabel(" Sales  ")

plt.legend(loc = "best") # we can explicitly give the location of legend or , we can simply best-which will automatically fits the best
plt.show()

# you can play with the width ;)     


# In[ ]:


#------------------------PIECHARTS-----------------------


'''
  So the command is pie ()
  
      shadow     - any shadow required
      startangle - angle from which the piechart starts
      explode    -  do you need any gap after each slice 
'''

plt.pie( city1_sales , explode =[0.1 , 0.1, 0,0,0.1] , labels = month , shadow = True , startangle = 0)
plt.title("PIECHART")
plt.legend(loc = "best")
plt.show()

# play with startangle to understand it 

#the white color gaps below are due to explode parameter 

# shadow ???? ahem ahem there there see see small black shadow at the edge 

