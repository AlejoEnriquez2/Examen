# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:42:23 2020

@author: alejo
"""
import numpy as np
from multiprocessing import Manager, Process
from EnriquezMancheno_Alejandro_ExamenMultiprocessingMetodos import Metodo1
import random
import time

num_procesos = 5
datosCant = 4000000
datos = [random.randrange(1,30) for i in range(datosCant)]
squared_sum = 0

inicio = 0
fin = 0


if __name__ == '__main__':
    with Manager() as manager:
        lista1 = manager.list()
        procesos = []
        pro = datosCant//num_procesos-1
        residuo = datosCant % num_procesos-1
        print(residuo)
        ti = time.time()
        for i in range(num_procesos):
            extra = pro+1 if i <= residuo else pro
            p = Process(target=Metodo1, args=(datos[inicio:inicio+extra], lista1))
            p.start()
            procesos.append(p)
            inicio = inicio + extra
        
        for p in procesos:
            p.join()
            p.terminate()
            
        tf = time.time()
        tt = (tf-ti)*1000
        print("Tiempo de procesamiento: ", tt)
            
            
            
        
        