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

def main():
    ctx = mul.get_context('spawn')
    # Build a pipe
    pipe = ctx.Pipe()

    # Pass an end of the pipe to process 1
    p1 = ctx.Process(target=proc1, args=(pipe[0],))

    # Pass the other end of the pipe to process 2
    p2 = ctx.Process(target=proc2, args=(pipe[1],))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

 # it's required to avoid RuntimeError if multiprocessing API was called on get_context('spawn')
if __name__ == '__main__':
    main()
