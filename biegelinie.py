# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 13:55:20 2020

@author: andre
"""
import numpy as np
import matplotlib.pyplot as plt
l=1
f=1
a=(1/3)*l
lager=(1/6*f*(l**2-2*l*a+a**2)*(a+2*l))/((l**3)/3)
print (lager)
x=(np.arange(0,l,0.01,float))

n=len(x)
print (n)
y=(np.zeros(n,float))
    
for i in range(0,n):
    y[i]=(-13/54)*(x[i]+(x[i])**3)
print (y)
    


plt.plot(x,y)