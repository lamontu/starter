# -*- coding: utf-8 -*-

from contextlib import contextmanager

@contextmanager
def file_manager(name, mode):
    try:
        print(f'opening file {name}')
        f = open(name, mode)
        yield f
    finally:
        print(f'closing file {name}')
        f.close()
        
with file_manager('test.txt', 'w') as f:
    f.write('hello world')

print('------------------------------------------')

class DummyResource(object):
    def __init__(self, tag):
        self.tag = tag
        print('Resource [%s]' % tag)
    
    def __enter__(self):
        print('[Enter %s]: Allocate resource.' % self.tag)
        return self 

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('[Exit %s]: Free resource.' % self.tag)
        if exc_tb is None:
            print('[Exit %s]: Exited without exception.' % self.tag)
        else:
            print('[Exit %s]: Exited with exception raised.' % self.tag)
            return False
        # return True  ## if exception is handled

with DummyResource('Normal'):
    print('[with-body] Run without exception.')
 
print('------------------------------------------')

with DummyResource('With-Exception'):
    print('[with-body] Run with exception')
    raise Exception
