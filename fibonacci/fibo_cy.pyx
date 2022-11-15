cpdef fibonacci_c(int n):
    if n < 0:
        print("1st fibonacci number = 0")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_c(n-1) + fibonacci_c(n-2)