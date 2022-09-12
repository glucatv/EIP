#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 09:08:46 2022

@author: gianluca
"""

# In[]

# input
x = 2

# introduzione delle variabili
g = x
counter = 0

while counter < 10:
    g = ( g + x/g )/2
    counter = counter + 1
    
print(g)


# In[]

# input
x = 3
eps = 0.000001

# introduzione delle variabili
g = x

while abs(g*g - x) > eps :
    g = ( g + x/g )/2
    
print(g)