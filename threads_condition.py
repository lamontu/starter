# -*- coding: utf-8 -*-

import threading
import time


def consumer(cond):
    with cond:
        print('consumer before wait')
        cond.wait()
        print('consumer after wait')


def producer(cond):
    with cond:
        print('producer before notifyall')
        cond.notifyAll()
        print('producer after notifyall')


condition = threading.Condition()

c1 = threading.Thread(name = 'c1', target = consumer, args = (condition,))
c2 = threading.Thread(name = 'c2', target = consumer, args = (condition,))

p = threading.Thread(name = 'p', target = producer, args = (condition,))

c1.start()
time.sleep(3)

c2.start()
time.sleep(3)

p.start()

 
