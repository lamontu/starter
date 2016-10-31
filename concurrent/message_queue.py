# -*- coding: utf-8 -*-

import os
import multiprocessing as mulpro
import time


# input worker
def inputQ(queue):
    info = str(os.getpid()) + '(put):' + str(time.time())
    queue.put(info)


# output worker
def outputQ(queue, lock):  # use lock to prevent messy print
    info = queue.get()
    lock.acquire()
    print(str(os.getpid()) + '(get):' + info)
    lock.release()


# Main
record1 = []
record2 = []
lock = mulpro.Lock()
queue = mulpro.Queue(3)


# input processes
for i in range(10):
    process = mulpro.Process(target=inputQ, args=(queue,))
    process.start()
    record1.append(process)

# output processes
for i in range(10):
    process = mulpro.Process(target=outputQ, args=(queue, lock))
    process.start()
    record2.append(process)

for p in record1:
    p.join()

queue.close()  # No more object will come, close the queue.

for p in record2:
    p.join()


