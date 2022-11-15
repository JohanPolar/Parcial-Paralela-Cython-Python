#cython: language_level=3
cimport cython
'''
Fecha 01 - Noviembre - 2022
Autor: Juan Camilo Rodriguez Fonseca
Materia: Parallel and Distributed Computing
Tema: Cython
'''


'''
Se instancia como función externa,
Se prepara para multihilo
'''
def bubbleSort(list array):
	cdef bint cambio = True
	cdef int i
	while cambio:
		cambio=False
		for i in range(len(array) - 1):
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
				cambio = True
	return array
