# -*- coding: utf-8 -*-
 
import time
 
def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2-t1)*1000 if unit == 'ms' else t2-t1
            print 'call %s() in %f %s'%(f.__name__,t,unit)
            return r
        return wrapper
    return perf_decorator
 
#@performance('ms') 不用装饰器
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
 
#手动装饰
factorial = performance('ms')(factorial)
print factorial(10)
print factorial.__name__
