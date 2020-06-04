# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:42:23 2020

@author: alejo
"""
import numpy as np
from multiprocessing import Manager, Process
from MetodosParalelos import *



def Metodo1(lista1, resultado):
    squared_sum = 0    
    for i in lista1:
        squared_sum += i * i

    raiz = squared_sum**(.5)
    
    for n in a:
        result.append(n/raiz)

    lista1.append(1)
    lista2.append(2)
    