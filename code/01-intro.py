#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 15:06:05 2022

@author: gianluca
"""

# Assegnazione: il valore dell'espressione a destra di =
# viene assegnato alla variabile a sinistra

x = 6

y = x**2+4*x + 2

print('il valore di x è ', x, ' ed il valore di y è ', y)


f = x/y

print(f)

d = x/2

print(type(d))

# l'esito di una divisione è sempre float

d = x//2 # divisione intera

print(type(d))

n = int('12') # conversione in intero
print(n)
print('12')

n = int(float('12.3')) # coversione in float e poi in intero
print(type(n))


print(7%5) # operatore modulo

# In[Funzioni]

# Definizione di funzioni

def radice_quadrata( x ):
    eps = 0.000001
    
    # introduzione delle variabili
    g = x
    
    while abs(g*g - x) > eps :
        g = ( g + x/g )/2
        
    return g
        
x = radice_quadrata( 2 )
y = radice_quadrata( 3 )
print(x+y)

# In[]

# Nuova versione della funzione radice_quadrata con eps
# che diventa un secondo  parametro

def radice_quadrata( x, eps):

    # introduzione delle variabili
    g = x
    
    while abs(g*g - x) > eps :
        g = ( g + x/g )/2
        
    return g

print(radice_quadrata(2, 0.0001))

# In[ATTENZIONE]

def radice_quadrata( x ):
    eps = 0.000001
    
    # introduzione delle variabili
    g = x
    
    while abs(g*g - x) > eps :
        g = ( g + x/g )/2
        
    return g
        
x = radice_quadrata( 2 )
y = radice_quadrata( 3 )
print(x+y)