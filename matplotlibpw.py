# -*- coding: utf-8 -*-
"""
Created on Sun May 21 10:20:44 2023

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,200)
x
y=np.sin(x)
y
# ------------------------------------
#plot
plt.plot(x,y,'--b',)
plt.figure(figsize=(8,4))
plt.xlabel("this is my x data")
plt.ylabel("this is my y data")
plt.title("this is my title")
plt.show()
-----------------------------------------
#scatter plot
x=np.random.rand(50)
y=np.random.rand(50)
colours=np.random.rand(50)
plt.scatter(x,y,c='b',alpha=.5,marker="x")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title('Random data')
----------------------------------------------
#bar graph
x=['a','b','c','d','e']
y=np.random.rand(5)
plt.bar(x,y)
plt.xlabel("this is my x data")
plt.ylabel("this is my y data")
plt.title("this is my bar plot")
------------------------------------------------
#barh plot(horizontal bar)
x=['a','b','c','d','e']
y=np.random.rand(5)
plt.barh(x,y)
plt.xlabel("this is my x data")
plt.ylabel("this is my y data")
plt.title("this is my barh plot")
-------------------------------------------------
#histogram
data=[1,2,3,4,5,1,2,3,6,7,8,1,2,3]
plt.hist(data)
--------------------------------------------
x=np.random.rand(50)
y=np.random.rand(50)
z=np.random.rand(50)
fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.scatter(x,y,z)
plt.show()






















x=[4,5,6,7,8,9]
y=[6,7,8,9,10,11]
plt.plot(x,y)








