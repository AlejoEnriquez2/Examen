# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:43:58 2020

@author: alejo
"""

from mpi4py import MPI
import numpy as np
import time
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
procesos = comm.Get_size()

numworkers = procesos - 1

datosCant = 4000000
datos = [random.randrange(1,30) for i in range(datosCant)]
result = []
resultado = []
squared_sum = 0

if rank==0:    
    p = datosCant//numworkers
    residuo = datosCant % numworkers
    inicio = 0
    tiempos = 0.0;
    ti = time.time()
    for i in range(1, procesos):
        extra = p+1 if i <= residuo else p
        comm.send(datos[inicio:inicio+extra], dest=i, tag=1)
        inicio = inicio + extra
        res= comm.recv(source=i, tag=1)
        tiempoRes= comm.recv(source=i, tag=2)
        resultado.append(res)
        #tiempos = tiempos + tiempoRes
        
    tf = time.time()
    tt = (tf-ti)*1000
    #print("Tiempo MPI: ", tt, "Resultado: ", resultado)
    print("Tiempo MPI: ", tt)

if rank > 0:
    inicioMpi = time.time()
    a = comm.recv(source=0, tag=1)
    
    for i in a:
        squared_sum += i * i

    raiz = squared_sum**(.5)
    
    for n in a:
        result.append(n/raiz)

    comm.send(result, dest=0, tag=1)
    
    finMpi =  time.time()   
    tRes = (finMpi - inicioMpi)*1000
    comm.send(tRes, dest=0, tag=2)
    print("Proceso :", rank, " Con la cantidad de datos: ",len(a) ," Tiempo: ", tRes)
   
    
    
    
    
    
    
