import cython

@cython.boundscheck(False)
@cython.wraparound(False)

def multiply(double [:,:] u, double [:,:] v, double [:,:] res):

    cdef int i, j, k
    cdef int m, n, p

    m = u.shape[0]
    n = u.shape[1]
    p = v.shape[1]


    with cython.nogil:
        for i in range(m):
            for j in range(p):
                res[i,j] = 0
                for k in range(n):
                    res[i,j] += u[i,k] * v[k,j]
        