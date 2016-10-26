# -*- coding: utf-8 -*- 

import dis 

code_obj = compile('sum([1, 2, 3])', '', 'single')

print('exec(code_obj) >>>>')
print(exec(code_obj))
print()

print('dis.dis(code_obj) >>>>')
print(dis.dis(code_obj))
print('---------------')
print('---------------')


def foo():
    m = 3
    n = 5
    def bar():
        print('id(m): %x' % id(m))
        print('id(n): %x' % id(n))
        a = 4
        return m + n + a
    return bar

print('foo.__code__ >>>>')
print(foo.__code__)
print()

print('bar = foo() >>>>')
bar = foo()
print('bar:', bar)
print()

print('bar.__closure__ >>>>')
print(bar.__closure__)
print()

print('bar() >>>>')
print(bar())
