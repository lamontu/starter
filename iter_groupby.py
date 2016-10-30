# -*- coding: utf-8 -*-

import itertools


chain_generator = itertools.chain([1, 2, 3], [7, 8, 9])

"""
chain_list = list(chain_generator)
print(chain_list)
"""

print(next(chain_generator))
print(next(chain_generator))

chain_list = list(chain_generator)
print(chain_list)

print('------------------------------------')

def height_class(h):
    if h > 180:
        return "tall"
    elif h < 160:
        return "short"
    else:
        return "middle"


friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]

friends = sorted(friends, key = height_class)
for m, n in itertools.groupby(friends, key = height_class):
    print(m)
    print(list(n))


