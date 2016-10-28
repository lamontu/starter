# -*- coding: utf-8 -*-

import signal

# Define signal handler function
def myHandler(signum, frame):
    print('I received:', signum)

# Register signal.SIGTSTP' handler
signal.signal(signal.SIGTSTP, myHandler)

signal.pause()

print('End of Signal Demo')
