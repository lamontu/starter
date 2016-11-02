# -*- coding: utf-8 -*-

import os.path


path = '/Users/yuxiaofei/python/starter/file_1.txt'

print(os.path.basename(path))
print(os.path.dirname(path))

info = os.path.split(path)
path2 = os.path.join('/', 'Users', 'yuxiaofei','python', 'starter', 
                     'file_2.xtx')

p_list = [path, path2]
print(os.path.commonprefix(p_list))


print(os.path.exists(path))

print(os.path.getsize(path))
print(os.path.getatime(path))
print(os.path.getmtime(path))

print(os.path.isfile(path))
print(os.path.isdir(path))


