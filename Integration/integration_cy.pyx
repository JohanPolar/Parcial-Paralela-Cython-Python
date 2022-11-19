from libc cimport math
import cython

@cython.boundscheck(False)
@cython.wraparound(False)


cdef double f(double x) nogil:
    return math.exp(-(x ** 2))

cdef double integrate_f(double a, double b, int N) nogil:
    cdef double s = 0
    cdef double dx = (b - a) / N
    cdef int i
    for i in range(N):
        s += f(a + i * dx)
    return s * dx


def iterate_function(int count, double a, double b, int N):
    #Se itera la función de integración 'count' veces
    cdef int i
    cdef double result

    with cython.nogil:
        for i in range(count):
            result = integrate_f(a, b, N)

    return result