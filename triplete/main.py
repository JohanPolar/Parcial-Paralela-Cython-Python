"""
Fecha: 01/11/2022
Autor: Roxanyffer Velasco Contreras
Computación Paralela y Distribuida
Principal: Llama a ambos programas Cy/Py
"""

from Triplete_Pitagorico_Matriz_CY import isTriplet as isTriplet_cy
from Triplete_Pitagorico_Matriz_PY import isTriplet
import random
import time

iteraciones = 30

carga1 = 500
carga2 = 1000
carga3 = 1500

range_gen = 1000

cargas = [random.sample(range(0,carga1+range_gen),carga1),random.sample(range(0,carga2+range_gen),carga2),random.sample(range(0,carga3+range_gen),carga3)]

print_format = "{:.5f},{:.5f}\n"

for i in range (len(cargas)):

    f = open(f"triplete{i}.csv","w")
    f.truncate()
    f.close()
 
    carga = cargas[i]

    with open(f"triplete{i}.csv","a") as archivo:
        archivo.write("Python,Cython\n")

    for j in range(iteraciones):
        init_time=time.time()
        isTriplet(carga,len(carga))
        end_time=time.time()

        time_python = end_time - init_time

        init_time=time.time()
        isTriplet_cy(carga,len(carga))
        end_time=time.time()

        time_cython = end_time - init_time

        with open(f"triplete{i}.csv","a") as archivo:
            archivo.write(print_format.format(time_python,time_cython))