# -*- coding: utf-8 -*-

import struct


print("calcsize('hhl'):", struct.calcsize('hhl'))
print("struct.pack('hhl', 1, 2, 3)")
print(struct.pack('hhl', 1, 2, 3), '\n')

print("===> big-endian")
print("calcsize('>hhl'):", struct.calcsize('>hhl'))
print("struct.pack('>hhl', 1, 2, 3)") 
print(struct.pack('>hhl', 1, 2, 3), '\n')

print("===> little-endian")
print("calcsize('<hhl'):", struct.calcsize('<hhl'))
print("struct.pack('<hhl', 1, 2, 3)")
print(struct.pack('<hhl', 1, 2, 3), '\n')


print("calcsize('lhh'):", struct.calcsize('lhh'))
print("struct.pack('lhh', 3, 1, 2)")
print(struct.pack('lhh', 3, 1, 2), '\n')

print("===> big-endian")
print("calcsize('>lhh'):", struct.calcsize('>lhh'))
print("struct.pack('>lhh', 3, 1, 2)")
print(struct.pack('>lhh', 3, 1, 2), '\n')

print("===> little-endian")
print("calcsize('<lhh'):", struct.calcsize('<lhh'))
print("struct.pack('<lhh', 3, 1, 2)")
print(struct.pack('<lhh', 3, 1, 2), '\n')


