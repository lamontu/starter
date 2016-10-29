# -*- coding:utf-8 -*-
class A(object):
    @staticmethod
    def staticMethod():
        print('staticFunc()')
    
    @classmethod
    def classMethod():
        print('classMethod()')

    def func():
        print('func()')

a = A()
print('A.staticMethod:', A.staticMethod)
print('A.classMethod:', A.classMethod)
print('A.func:', A.func)

print('a.staticMethod:',a.staticMethod)
print('a.classMethod:', a.classMethod)
print('a.func:', a.func)

print()

print(type(A.staticMethod))
print(type(A.classMethod))
print(type(A.func))

print(type(a.staticMethod))
print(type(a.classMethod))
print(type(a.func))
