# -*- coding: utf-8 -*-

import pickle

# define class
class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'

summer = Bird() # construct an object

'''
picklestring = pickle.dumps(summer) # serialize the object
'''

fn = 'serialize.pkl'
with open(fn, 'wb') as f:                  # open binary file with write-mode
    picklestring = pickle.dump(summer, f)  # serialize and save the object summer
