# -*- coding: utf-8 -*-

import threading
import time
import os

def doChore():
    time.sleep(0.5)

class BoothThread(threading.Thread):
    def __init__(self, tid, monitor):
        self.tid = tid
        self.monitor = monitor
        threading.Thread.__init__(self)
    def run(self):
        while True:
            # acquire lock if other thread is not holding the lock, or wait 
            monitor['lock'].acquire() 

            if monitor['tick'] != 0: 
                monitor['tick'] = monitor['tick'] - 1
                print('%d,' % self.tid, 'now left:', monitor['tick'])
                doChore()
            else:
                print('Thread_id: %d.' % self.tid, "No more tickets.")
                os._exit(0)
            monitor['lock'].release()

            doChore()  # non-critical operations

monitor = {'tick': 100, 'lock': threading.Lock()}

# start 10 threads
for k in range(10):
    new_thread = BoothThread(k, monitor)
    new_thread.start()
