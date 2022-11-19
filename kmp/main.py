from kmp_algorithm import KMP
from kmp_algorithm_cy import KMP as KMP_cy
import string
import random
import time

iteraciones = 30

"""
* Los textos se generarán aletoriamente de forma automática con las siguientes longitudes:
    * 500000 caracteres
    * 1000000 caracteres
    * 2000000 caracteres
* Los patrones de búsqueda serán de 5 caracteres cada uno y serán aleatorios
"""

carga1 = 5000000
carga2 = 10000000
carga3 = 20000000

texts = [''.join(random.choice(string.ascii_uppercase) for i in range(carga1)), ''.join(random.choice(string.ascii_uppercase) for i in range(carga2)), ''.join(random.choice(string.ascii_uppercase) for i in range(carga3))]

patterns = [''.join(random.choice(string.ascii_uppercase) for i in range(5)) for j in range(3)]

print_format = "{:.5f},{:.5f}\n"


#print("Cargas generadas")
for i in range (len(texts)):

    #Clears csv
    f = open(f"kmp{i}.csv","w")
    f.truncate()
    f.close()

    text = texts[i]
    pattern = patterns[i]
    #print("Patrón -> {}\nCarga ->{}".format(text,pattern))

    with open(f"kmp{i}.csv","a") as archivo:
        archivo.write("Python,Cython\n")

    for j in range(iteraciones):
        init_time=time.time()
        KMP(text,pattern)
        end_time=time.time()

        time_python = end_time - init_time

        init_time=time.time()
        KMP_cy(text,pattern)
        end_time=time.time()

        time_cython = end_time - init_time

        with open(f"kmp{i}.csv","a") as archivo:
            archivo.write(print_format.format(time_python,time_cython))

