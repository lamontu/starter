# -*- coding: utf-8 -*-

import inspect


class Base(object):
    def __init__(self):
        print('Base init')


class Medium1(Base):
    def __init__(self):
        super(Medium1, self).__init__()  # Replace 'Base.__init__(self)'      
        print('Medium1 init')


class Medium2(Base):
    def __init__(self):
        super(Medium2, self).__init__()  # Replace 'Base.__init__(self)'    
        print('Medium2 init')


class Leaf(Medium1, Medium2):
    def __init__(self):
        """
        mro = [Leaf, Medium1, Medium2, Base]
        super(type, obj).__init__() 
        search start from the one next to type 
        """        
        super(Leaf, self).__init__()  # search from Medium1 
        # super(Medium1, self).__init__()  # search from Medium2 
        # super(Medium2, self).__init__()  # search from Base 

        print('Leaf init')


print('inspect.getmro(Leaf) >>>>')
print(inspect.getmro(Leaf))

print('leaf = Leaf() >>>>')
leaf = Leaf()
