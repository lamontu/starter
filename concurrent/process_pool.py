# -*- coding: utf-8 -*-

import multiprocessing
import subprocess
import time
import sys


filehandler = open('process_pool_web.txt','r')
filehandler.seek(0)

l = list()
for line in filehandler:
    line = line.strip('\n')
    l.append(line)
lineCount = len(l)


def downloadPage(x):
    print('<<<<<< Start to download %s --- %s >>>>>>' % (x, l[x]))
    cmd = ['wget', '-c', ('%s' % l[x]), '-O', ('index-%s.html' % str(x))] 
    child = subprocess.Popen(cmd)
    child.wait()
    print('<<<<<< Finish download %s --- %s >>>>>>' % (x, l[x]))


pool = multiprocessing.Pool(3)
for i in range(lineCount):
    res = pool.apply_async(downloadPage, (i,))

pool.close()
pool.join()

if res.successful():
    print('successful')


