def fib(int n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

#
cdef extern from "c_fib.c":
    int c_fib(int n)

def fib_c(n):
    return c_fib(n)