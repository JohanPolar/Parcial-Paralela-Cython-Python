from os import lseek


'''
Fichero de compilación, convierte el .pyx en un .so (Shared Object)
'''

from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize("Triplete_Pitagorico_Matriz_CY.pyx", language_level = "3"))

setup(ext_modules = exts)