cdef _str_add(char *x, char *y):
    return int(x) + int(y)

cdef _str_sub(char *x, char *y):  #减法
    return int(x) - int(y)

def str_add(x, y):
    return _str_add(x, y)
def str_sub(x, y):
    return _str_sub(x, y)

# from b import _add_1_100, _get_date
# import b
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

def add_1_100(x, y):
    '''
    计算2数的累加
    :param x: 最小数
    :param y: 最大数
    :return: 总和
    '''
    return _add_1_100(x, y)

from datetime import datetime

def get_date(d: datetime):
    '''
    获取日期字符串
    :param d:datetime
    :return:字符串 格式:%Y%m%d-%H:%M:%S
    '''
    return _get_date(d)
