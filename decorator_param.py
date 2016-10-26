# -*- coding: utf-8 -*-
 
import time, functools
 
def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            t_start = time.time()
            result = f(*args, **kw)
            t_end = time.time()
            t_cost = t_end - t_start
            if unit == 'ms':
                t_cost = t_cost * 1000
            
            print('call %s() in %f%s' % (f.__name__, t_cost, unit))
            return result
        return wrapper
    return perf_decorator
 

@performance('ms')
def factorial(n):
    return functools.reduce(lambda x,y: x*y, range(1, n+1))
 
'''
# manually decorating
factorial = performance('ms')(factorial)
'''

print(factorial.__name__)

print(factorial(10))

