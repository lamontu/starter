# -*- coding: utf-8 -*-

import signal

# Define signal handler function
def myHandler(signum, frame):
    print('I received:', signum)


# Register signal.SIGTSTP's handler
# SIGTSTP = 18, signal generated from keyboard 
signal.signal(signal.SIGTSTP, myHandler)

signal.pause()

print('End of Signal Demo')
