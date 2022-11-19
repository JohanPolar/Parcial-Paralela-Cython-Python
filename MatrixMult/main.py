'''
Fecha 01 - Noviembre - 2022
Autor: Santiago Nohra Nieto
Materia: Parallel and Distributed Computing
Tema: Cython
La idea principal es exportar un '.csv' con la toma de tiempos
'''

import matrix_mult_cy
import matrix_mult_py
import time
import numpy as np

cargas = [500, 1000, 1500]
iteraciones = 30
print_format = "{:.5f},{:.5f}\n"

for i, carga in enumerate(cargas):
    f = open(f"matrix{i}.csv","w")
    f.truncate()
    f.close()

    with open(f"matrix{i}.csv","a") as archivo:
        archivo.write("Python,Cython\n")


    u = np.random.random((200, carga))
    v = np.random.random((carga, 100))
    res = np.zeros((u.shape[0], v.shape[1]))
    res2 = np.zeros((u.shape[0], v.shape[1]))
    
    for j in range(iteraciones):
        init_time = time.time()
        matrix_mult_py.multiply(u, v, res)
        end_time = time.time()
        time_python = end_time - init_time

        init_time = time.time()
        matrix_mult_cy.multiply(u, v, res)
        end_time = time.time()
        time_cython = end_time - init_time


        with open(f"matrix{i}.csv","a") as archivo:
            archivo.write(print_format.format(time_python,time_cython))