# -*- coding: utf-8 -*-

import threading


def doOnEvent(event):  # pass a threading.Event object as parameter
    print('start')
    event.wait()  # block until flag == True
    print('execute')


event_obj = threading.Event()  # construct a threading.Event object 


for i in range(3):
    # contruct a thread
    t = threading.Thread(target = doOnEvent, args = (event_obj,))  

    # Method run() of object t will execute statements in doOnEvent to event.wait() 
    t.start()  


event_obj.clear()  # flag = False

inp = input('input:')

while True:
    if inp == 'RecognizedEvent':
        event_obj.set()  # flag = True, then the thread continue to run
        break
    else:
        print("not 'RecognizedEvent'")
        inp = input('input:')
