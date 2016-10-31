# -*- coding: utf-8 -*-

import multiprocessing
import time
import os

def f(x):
    print('Task %s start...' % x)
    for i in range(1, 6):
        print('Step %s ------ Task %s (%s)' % (i, x, os.getpid()))
        time.sleep(1)
    print('Task %s end' % x)


def main():
    pool = multiprocessing.Pool(processes=3)  # set the processes max number 3
    lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    for i in lst: 
        result = pool.apply_async(f, (i,))

    pool.close()
    pool.join()
    if result.successful():
        print('successful')


if __name__ == '__main__':
    main()


