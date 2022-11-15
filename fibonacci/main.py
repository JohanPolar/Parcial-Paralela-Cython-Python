import fibo_py
import fibo_cy
import time

carga = 25

formato_datos = "{:.5f}, {:.5f}\n"
with open("fibo.csv", "a") as archivo:
    archivo.write('Python,Cython\n')

for i in range(30):
    init_time = time.time()
    fibo_py.Fibonacci(carga)
    end_time = time.time()

    time_python = end_time - init_time

    init_time=time.time()
    fibo_cy.fibonacci_c(carga)
    end_time=time.time()

    time_cython = end_time - init_time

    with open("fibo.csv", "a") as archivo:
        archivo.write(formato_datos.format(time_python, time_cython))