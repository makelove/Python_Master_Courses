cdef public str_add(str1, str2):  #cdef替换了def，并加了public关键字，表示这个函数要导出。
    return int(str1) + int(str2)
