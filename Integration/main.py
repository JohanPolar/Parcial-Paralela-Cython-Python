'''
Fecha 01 - Noviembre - 2022
Autor: Santiago Nohra Nieto
Materia: Parallel and Distributed Computing
Tema: Cython
La idea principal es exportar un '.csv' con la toma de tiempos
'''

import integration_py
import integration_cy
import time

repeticiones = 500
cargas = [40000, 80000, 120000]
iteraciones = 30

print_format = "{:.5f},{:.5f}\n"


for i, carga in enumerate(cargas):
    f = open(f"integration{i}.csv","w")
    f.truncate()
    f.close()

    with open(f"integration{i}.csv","a") as archivo:
        archivo.write("Python,Cython\n")

    for j in range(iteraciones):
        init_time = time.time()
        integration_py.iterate_function(repeticiones, 0.0, 10.0, carga)
        end_time = time.time()
        time_python = end_time-init_time

        init_time = time.time()
        integration_cy.iterate_function(repeticiones, 0.0, 10.0, carga)
        end_time = time.time()
        time_cython = end_time-init_time

        with open(f"integration{i}.csv","a") as archivo:
            archivo.write(print_format.format(time_python,time_cython))
