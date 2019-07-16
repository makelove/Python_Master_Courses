cdef int _add_1_100(int x, int y):
    cdef int sum1 = 0
    cdef int temp
    for temp in range(x, y + 1):
        sum1 += temp
    return sum1



cdef char *_get_date(d):
    cdef char *date
    s1 = d.strftime('%Y%m%d-%H:%M:%S')
    date = s1

    return date

