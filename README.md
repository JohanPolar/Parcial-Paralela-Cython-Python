# Medida de rendimiento: Órbitas planetarias

## Introducción

Con el objetivo de indagar y adquirir mayores conocimientos tanto en los lenguajes de programación Python y Cython como en el rendimiento y los beneficios de cada uno de estos, se realizan las prácticas y las pruebas de 6 algoritmos (Burbuja, Fibonacci, Kmp, Triplete, multiplicación de matrices e Integración matemática de N iteraciones), realizando las tomas de rendimiento correspondientes. Estos ejercicios tienen como finalidad realizar un análisis práctico e interactivo para diferenciar los procesos y el avance en rendimiento que representa y significa en concreto uno frente al otro, tomando como referencia sustancial el hecho de que se realizará una comparación entre los rendimientos de los programas Cython y Python. Si bien comúnmente Python es el lenguaje más popular actualmente entre los dos, cabe aclarar que Cython es un lenguaje de programación que combina Python con el sistema de tipos estáticos de C y C++, lo que sin duda alguna es una unificación de las mejores características de estos grandes e increíbles lenguajes de programación.

## Desarrollo

### Toma de datos

Para cada uno de los algoritmos seleccionados se encuentra un directorio con la implementación de los algoritmos en ***python*** y ***cython***, la clase principal, su **Makefile** y los ficheros *.csv* utilizados para el análisis de rendimiento. Para cada algoritmo se realizaron 30 iteraciones por cada una de las tres entradas (cargas) seleccionadas.

#### Directorios - Algoritmos

* [Ordenamiento Burbuja](./Burbuja/)

* [Integración matemática](./Integration/)

* [Multiplicación de matrices](./MatrixMult/)

* [Serie fibonacci](./fibonacci/)

* [Triplete pitagórico](./triplete/)

* [KMP (Knuth-Morris-Pratt)](./kmp/)


### Ejecución local

Para hacer la reproducción satisfactoria del experimento se debe:

Clonar el repositorio

`git clone https://github.com/JohanPolar/Parcial-Paralela-Cython-Python.git`

Acceder al directorio

`cd Parcial-Paralela-Cython-Python`

Compilar el módulo de *cython*

`make all`

>Esto permitirá acceder a los recursos descritos en los archivos __*.pyx__ desde *python* y *C*.

Con ello hecho es posible hacer la ejecución del cada algoritmo al realizar el comando  `python3 main.py` dentro de cada directorio, esto generará automáticamente los datos obtenidos durante la experimentación.En el [notebook](https://colab.research.google.com/drive/1vrK2rAlm4SVyNW92EXZGEd9Ks8SI6XHB?usp=sharing) adjunto se hacen un análisis de la experimentación realizada. Si desea hacer cambios a la experimentación se recomienda dirigirse a las *recomendaciones* allí expuestas.



## Conclusión

Teniendo en cuenta el análisis realizado, de la mano con los procesos y el comportamiento que se visualiza en las gráficas, para los resultados de la toma de rendimiento de los algoritmos planteados anteriormente en los lenguajes de programación Python y Cython respectivamente, se logra comprender y analizar que al generar los procesos correspondientes, claro está, de la mano con el uso e implementación de buenas prácticas de programación a nivel algorítmico, se logra generar una interpretación basada fundamentalmente en el hecho de que Cython, como se ha mencionado anteriormente, es una fusión de muchas de las mejores características de Python, C y C++. Para quien conoce a nivel teórico y fundamentalmente práctico los lenguajes de programación mencionados, antes del diseño de Cython, habrán logrado generar una postura de reconocimiento y apreciación ante este, debido a que es un lenguaje de programación para simplificar la escritura de módulos de extensión para Python en C y C++. Cython posee una sintaxis bastante similar a Python pero con algunos agregados, como generar llamados de funciones de C y C++ y brindando la posibilidad de emplear distintos tipos estáticos en las variables.

Según este preámbulo teórico y los resultados obtenidos en las prácticas realizadas a los algoritmos, es acertado afirmar que Cython contribuye significativamente al rendimiento de un equipo, lo que para cualquier profesional de la computación representa una característica relevante debido a que no es necesario realizar un sacrificio tan grande del rendimiento al realizar cualquier proceso, sino que se obtienen resultados óptimos en las actividades realizadas sin comprometer unidades de rendimiento y recursos adicionales en la práctica. Siempre recomendando realizar una captura de datos que no se vea perjudicada por procesos web adicionales que generen basura en los datos recopilados.

> Para un mayor análisis dirigirse al [notebook](https://colab.research.google.com/drive/1vrK2rAlm4SVyNW92EXZGEd9Ks8SI6XHB?usp=sharing) adjunto
