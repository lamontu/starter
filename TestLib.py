# -*- coding: utf-8 -*-

'''
  # TestLib.py
  # When executin TestLib.py, __name__ is __main__.
  # When TestLib.py is imported, __name__ is TestLib
'''

print('------ >>>>>>')

def lib_func(a):
    return a + 10

def lib_func_another(b):
    return b + 20

if __name__ == '__main__':
    test = 101
    print(lib_func(test))

print('__name__:', __name__)

print('<<<<<< ------')
