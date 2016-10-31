# -*- coding: utf-8 -*-

import multiprocessing as mul
import os


def proc1(pipe):
    print('process 1 >>>>')
    print('proc1 pid:',os.getpid()) 
    pipe.send('hello')
    print('proc1 rec:', pipe.recv())
    print('process 1 <<<<')


def proc2(pipe):
    print('process 2 >>>>')
    print('proc2 pid:',os.getpid()) 
    print('proc2 rec:', pipe.recv())
    pipe.send('hello, too')
    print('process 2 <<<<')


# Build a pipe
pipe = mul.Pipe()


# Pass an end of the pipe to process 1
p1 = mul.Process(target=proc1, args=(pipe[0],))

# Pass the other end of the pipe to process 2
p2 = mul.Process(target=proc2, args=(pipe[1],))

p1.start()
p2.start()
p1.join()
p2.join()


