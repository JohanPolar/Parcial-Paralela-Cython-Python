import math
import time


def f(x):
    return math.exp(-(x ** 2))


def integrate_f(a, b, N):
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx


def iterate_function(count, a, b, N):
    #Se itera la función de integración 'count' veces
    for i in range(count):
        result = integrate_f(a, b, N)

    return result