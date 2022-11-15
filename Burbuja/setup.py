'''
Fecha 01 - Noviembre - 2022
Autor: Juan Camilo Rodriguez Fonseca
Materia: Parallel and Distributed Computing
Tema: Cython
'''
from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize('Burbuja_cy.pyx'))

setup(ext_modules = exts)
