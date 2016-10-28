# -*- coding: utf-8 -*-

import signal
import time

def myHandler(signum, frame):
    print("Now, it's the time")

    # must have this process, or RuntimeError will occur.
    # RuntimeError: reentrant call inside <_io.BufferedWriter name='<stdout>'>
    signal.alarm(5)

    # exit()  
 

signal.signal(signal.SIGALRM, myHandler)
signal.alarm(5)

while True:
    time.sleep(1)
    print('Not yet')
