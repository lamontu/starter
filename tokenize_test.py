# -*- coding: utf-8 -*-

from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
from io import BytesIO
from decimal import Decimal


def decistmt(s):
    result = []
    g = tokenize(BytesIO(s.encode('utf-8')).readline)
    for toknum, tokval, _, _, _ in g:
        if toknum == NUMBER and '.' in tokval:
            result.extend([
                (NAME, 'Decimal'),
                (OP, '('),
                (STRING, repr(tokval)),
                (OP, ')')
            ])  
        else:
            result.append((toknum, tokval))
    return untokenize(result).decode('utf-8')


s = 'print(+21.3e-5*-.1234/81.7)'

print('>>>> print(s)') 
print(s)
print('>>>> print(decistmt(s))')
print(decistmt(s))

print('>>>> exec(s)')
exec(s)
print('>>>> exec(decistmt(s))')
exec(decistmt(s))


