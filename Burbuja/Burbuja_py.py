'''
Fecha 01 - Noviembre - 2022
Autor: Juan Camilo Rodriguez Fonseca
Materia: Parallel and Distributed Computing
Tema: Cython
'''
def bubbleSort(array):
	cambio = True
	while cambio:
		cambio=False
		for i in range(len(array) - 1):
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
				cambio = True
	return array
