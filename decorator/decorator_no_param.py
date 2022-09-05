# -*- coding: utf-8 -*-

import time, functools

def performance(f):
    def fn(*args, **kw):
        t_start = time.time()
        result = f(*args, **kw)
        t_end = time.time()
        print('call %s() in %fs' % (f.__name__, t_end - t_end))
        return result
    return fn

@performance
def factorial(n):
    return functools.reduce(lambda x, y: x * y, range(1, n + 1))

print(factorial.__name__)

print(factorial(10))
