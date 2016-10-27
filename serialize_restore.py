# -*- coding: utf-8 -*-

import pickle

# define the class before deserializing
class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'

fn = 'serialize.pkl'
with open(fn, 'rb') as f:
    summer = pickle.load(f) # read file and build object

print(dir(summer)) #  object summer has been successfully rebuild
