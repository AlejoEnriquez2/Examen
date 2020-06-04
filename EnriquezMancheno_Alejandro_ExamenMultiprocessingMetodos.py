# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:42:23 2020

@author: alejo
"""

def Metodo1(lista1, resultado):
    squared_sum = 0    
    for i in lista1:
        squared_sum += i * i

    raiz = squared_sum**(.5)
    
    for n in lista1:
        resultado.append(n/raiz)
        
    print("Devuelve valor ")
    